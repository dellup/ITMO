function Get-NetworkDetails {
    $AdapterName = Select-NetworkAdapter
    
    $adapter = Get-NetAdapter -Name $AdapterName
    if ($adapter) {
        Write-Host "===== Сведения о сетевом адаптере ====="
        Write-Host "Имя: $($adapter.Name)"
        Write-Host "Модель: $($adapter.InterfaceDescription)"
        Write-Host "Состояние соединения: $($adapter.Status)"
        Write-Host "Скорость соединения: $($adapter.LinkSpeed)"
        Write-Host "Режим работы: $($adapter.Duplex)"
    } else {
        Write-Host "Адаптер с именем '$AdapterName' не найден."
    }
}

function Configure-DHCP {
    $AdapterName = Select-NetworkAdapter
    if ($AdapterName) {
        Set-NetIPInterface -InterfaceAlias $AdapterName -Dhcp Enabled
        Set-DnsClientServerAddress -InterfaceAlias $AdapterName -ResetServerAddresses
        Write-Host "DHCP успешно настроен для адаптера: $AdapterName."
    } else {
        Write-Host "Ошибка: Адаптер не найден."
    }
}

function Convert-SubnetMaskToPrefix {
    param (
        [string]$SubnetMask
    )
    
    $maskParts = $SubnetMask -split '\.' | ForEach-Object { [convert]::ToString([int]$_, 2) }
    return ($maskParts -join '').ToCharArray() -match '1' | Measure-Object | Select-Object -ExpandProperty Count
}

function Configure-StaticIP {
    $AdapterName = Select-NetworkAdapter
    if ($AdapterName) {
        $IPAddress = Read-Host "Введите IP-адрес "
        $SubnetMask = Read-Host "Введите маску подсети "
        $PrefixLength = Convert-SubnetMaskToPrefix -SubnetMask $SubnetMask
        $Gateway = Read-Host "Введите шлюз "
        $DNS = Read-Host "Введите адрес DNS-сервера "
        
        if (Get-NetAdapter -Name $AdapterName) {
            New-NetIPAddress -InterfaceAlias $AdapterName -IPAddress $IPAddress -PrefixLength $PrefixLength -DefaultGateway $Gateway
            Set-DnsClientServerAddress -InterfaceAlias $AdapterName -ServerAddresses $DNS
            Write-Host "Статический IP успешно настроен."
        } else {
            Write-Host "Ошибка: Указанный адаптер не найден."
        }
    } else {
        Write-Host "Ошибка: Адаптер не выбран."
    }
}

function Display-Menu {
    Write-Host "============================="
    Write-Host "  Настройка сетевого адаптера  "
    Write-Host "============================="
    Write-Host "1. Включить DHCP"
    Write-Host "2. Настроить статический IP"
    Write-Host "3. Показать информацию об адаптере"
    Write-Host "4. Выйти"
}

function Select-NetworkAdapter {
    $adapters = Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }
    
    if ($adapters.Count -eq 0) {
        Write-Host "Нет доступных активных адаптеров."
        return $null
    }
    
    Write-Host "Выберите сетевой адаптер:"
    $adapters | ForEach-Object { Write-Host "$($_.Name) - $($_.InterfaceDescription)" }
    
    $selection = Read-Host "Введите номер адаптера (например, 1 для первого)"
    
    if ($selection -match '^\d+$' -and $selection -gt 0 -and $selection -le $adapters.Count) {
        return $adapters[$selection - 1].Name
    } else {
        Write-Host "Ошибка: Неверный выбор. Попробуйте снова."
        return Select-NetworkAdapter
    }
}

while ($true) {
    Display-Menu
    $selection = Read-Host "Выберите номер действия"
    
    switch ($selection) {
        "1" { Configure-DHCP }
        "2" { Configure-StaticIP }
        "3" { Get-NetworkDetails }
        "4" { break }
        default { Write-Host "Ошибка: Некорректный ввод, попробуйте снова." }
    }
}
