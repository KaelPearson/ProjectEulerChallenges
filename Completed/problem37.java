/*
    https://projecteuler.net/problem=37

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
*/
package Completed;
import java.util.*;
public class problem37 {
    public static void main(String args[]){
        ArrayList<Integer> primes = getAllPrimesUnder(1000000);
        System.out.println(checkIfTrunPrime(3797, primes));
        int count = 0;
        int index = 10;
        int sum = 0;
        while(count < 11){
            if(checkIfTrunPrime(index, primes) == true){
                sum += index;
                count++;
                System.out.println(index);
            }
            index++;
        }
        System.out.println(sum);
    }
    public static boolean checkIfTrunPrime(int num, ArrayList<Integer> primes){
        int[] rightVartiations = getRightVariations(num);
        int[] leftVariations = getLeftVariations(num);
        for(int i = 0; i < rightVartiations.length; i++){
            if(binarySearch(primes, rightVartiations[i]) == -1){
                return false;
            }
            if(binarySearch(primes, leftVariations[i]) == -1){
                return false;
            }
        }
        return true;
    }
    public static ArrayList<Integer> getAllPrimesUnder(int limit){
        ArrayList<Integer> primes = new ArrayList<Integer>();
        int[] numList = new int[limit-1];
        for(int i = 2; i <= limit; i++){
            numList[i-2] = i;
        }
        for(int i = 2; i < Math.sqrt(limit) + 1; i++){
            for(int j = i - 1; j < numList.length; j++){
                if(numList[j] % i == 0){
                    numList[j] = 0;
                }
            }
        }
        for(int i = 0; i < numList.length; i++){
            if(numList[i] != 0){
                primes.add(numList[i]);
            }
        }
        return primes;
    }
    public static int[] getRightVariations(int num){
        String strNum = Integer.toString(num);
        int strNumLength = strNum.length();
        int[] arr = new int[strNumLength];
        for(int i = 0; i < strNumLength; i++){
            String subString = strNum.substring(0,i + 1);
            arr[i] = Integer.parseInt(subString);
        }
        return arr;
    }
    public static int[] getLeftVariations(int num){
        String strNum = Integer.toString(num);
        int strNumLength = strNum.length();
        int[] arr = new int[strNumLength];
        for(int i = 0; i < strNumLength; i++){
            String subString = strNum.substring(i,strNumLength);
            arr[i] = Integer.parseInt(subString);
        }
        return arr;
    }
    public static int binarySearch(ArrayList<Integer> arr, int key){
        int index = Collections.binarySearch(arr, key);
        if(index < 0){
            index = -1;
        }
        return index;
    }
}
