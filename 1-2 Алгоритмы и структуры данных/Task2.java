import java.math.BigInteger;
import java.util.*;
import java.util.stream.IntStream;

public class Task2 {
    public static String init() {
        int[] primes = new int[250];
        int ind = 0;
        for (int i = 2; i < 10000; i++) {
            if (prime(i)) {
                primes[ind] = i;
                ind++;
            }
            if (ind == 250) break;
        }
        String s = "";
        BigInteger[] f = fib();
        for (int i = 0; i < 250; i++) {
            s = s + String.valueOf(primes[i]) + String.valueOf(f[i]);
        }
        return s;
    }
    public static BigInteger[] fib() {
        BigInteger[] fibonacciArray = new BigInteger[250];
        fibonacciArray[0] = new BigInteger("0");
        fibonacciArray[1] = new BigInteger("1");

        for (int i = 2; i < 250; i++) {
            fibonacciArray[i] =  fibonacciArray[i-1].add(fibonacciArray[i-2]);
        }

        return fibonacciArray;
    }
    public static boolean prime(int n) {
        int d = 2;
        while (d * d <= n) {
            if (n%d==0) return false;
            d++;
        }
        return true;
    }

    public static int naiveAlg(String s) {
        int[] numbers = new int[90];
        int k = 0;
        for (int i = 10; i < 100; i++) {
            for (int j = 0; j < s.length()-1; j++) {
                if ((Integer.parseInt(s.substring(j,j+1)) == i/10) && (Integer.parseInt(s.substring(j+1,j+2)) == i%10)) {
                    numbers[k]++;
                }
            }
            k++;
        }
        int maxim = Arrays.stream(numbers).max().getAsInt();
        return IntStream.range(0, numbers.length).filter(i -> numbers[i] == maxim).findFirst().orElse(-1) + 10;
    }

    public static int rabinKarpAlg(String s) {
        int[] numbers = new int[90];
        int k = 0;
        int x = 10;
        for (int i = 10; i < 100; i++) {
            int hashI = (i/10)*x + (i%10);
            for (int j = 0; j < s.length()-1; j++) {
                int str = Integer.parseInt(s.substring(j,j+2));
                int hash = (str/10)*x + (str%10);
                if (hash == hashI) {
                    if ((str/10 == i/10) && (str%10 == i%10)) {
                        numbers[k]++;
                    }
                }
            }
            k++;
        }
        int maxim = Arrays.stream(numbers).max().getAsInt();
        return IntStream.range(0, numbers.length).filter(i -> numbers[i] == maxim).findFirst().orElse(-1) + 10;

    }
    public static int BoyerMooreAlg(String s) {
        int[] numbers = new int[90];
        int l = 0;
        for (int k = 10; k < 100; k++) {
            String pattern = String.valueOf(k);
            int patternSize = pattern.length();
            int textSize = s.length();

            // Создаем таблицу смещений для цифр в паттерне
            int[] shiftTable = new int[10];
            for (int j = 0; j < 10; j++) {
                shiftTable[j] = patternSize;
            }
            shiftTable[Character.getNumericValue(pattern.charAt(0))] = patternSize - 1;
//            Как работает таблица смещений
//            Для каждого символа из паттерна создается запись в таблице, где указывается, на сколько можно сдвинуть паттерн при несовпадении этого символа.
//            Если символ встречается в паттерне, то смещение будет равно размер_паттерна - индекс_символа - 1. Это позволяет перескочить все предыдущие вхождения этого символа в паттерне.


            int i = 0, j; // i - для позиции  в строке, j - для паттерна

            while ((i + patternSize) <= textSize) {
                j = patternSize - 1;

                while (s.charAt(i + j) == pattern.charAt(j)) {
                    j--;
                    if (j < 0) {
                        numbers[l]++;
                        break; // Добавляем break, чтобы выйти из внутреннего цикла
                    }
                }


                if (j < 0) {
                    i += patternSize; // Сдвигаем на размер паттерна
                } else {
                    i += shiftTable[Character.getNumericValue(s.charAt(i + patternSize - 1))];

                }
            }
            l++;
        }
        int maxim = Arrays.stream(numbers).max().getAsInt();
        return IntStream.range(0, numbers.length).filter(i -> numbers[i] == maxim).findFirst().orElse(-1) + 10;
    }

    static int[] prefixFunction(String pattern) {
        int [] values = new int[pattern.length()];
        for (int i = 1; i < pattern.length(); i++) {
            int j = 0;
            while (i + j < pattern.length() && pattern.charAt(j) == pattern.charAt(i + j)) { // ищем себя же внутри себя
                values[i + j] = Math.max(values[i + j], j + 1);
                j++;
            } // в результате получим массив, где максимальное значение будет равняться длине самого длинного суффикса, совпадающего с префексом
        }
        return values;
    }


    public static int KMPAlg(String text) {
        int[] numbers = new int[90];
        int l = 0;
        for (int k = 10; k < 100; k++) {
            int[] prefixFunc = prefixFunction(String.valueOf(k));

            int i = 0;
            int j = 0;

            while (i < text.length()) {
                if (String.valueOf(k).charAt(j) == text.charAt(i)) {
                    j++;
                    i++;
                }
                if (j == String.valueOf(k).length()) {
                    numbers[l]++;
                    j = prefixFunc[j - 1]; //берем то значение, куда нам надо вернуться, чтобы не потерять возможное наложенное значение
                } else if (i < text.length() && String.valueOf(k).charAt(j) != text.charAt(i)) {
                    if (j != 0) {
                        j = prefixFunc[j - 1];
                    } else {
                        i++;
                    }
                }
            }
            l++;
        }
        int maxim = Arrays.stream(numbers).max().getAsInt();
        return IntStream.range(0, numbers.length).filter(i -> numbers[i] == maxim).findFirst().orElse(-1) + 10;
    }


    public static void main(String[] args) {
        System.out.println(naiveAlg(init()));
        System.out.println(rabinKarpAlg(init()));
        System.out.println(BoyerMooreAlg(init()));
        System.out.println(KMPAlg(init()));
    }
}
