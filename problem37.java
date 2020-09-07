/*
    https://projecteuler.net/problem=37

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
*/
import java.util.Arrays;
public class problem37 {
    public static void main(String args[]){
        int num = 3797;
        int[] rightVartiations = getRightVariations(num);
        int[] leftVariations = getLeftVariations(num);
        System.out.println("Right " + Arrays.toString(rightVartiations));
        System.out.println("Left " + Arrays.toString(leftVariations));
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
}
