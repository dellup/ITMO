import asyncio
import aiofiles

async def read_and_count_chars(file_name):
    async with aiofiles.open(file_name, 'r') as file:
        data = await file.read()
        char_count = len(data)
    return file_name, char_count

async def process_files(files):
    tasks = [read_and_count_chars(file) for file in files]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    files = ['file1.txt', 'file2.txt', 'file3.txt']  # Список файлов для обработки

    results = await process_files(files)

    for file, char_count in results:
        print(f'Файл {file} содержит {char_count} символов.')

asyncio.run(main())
