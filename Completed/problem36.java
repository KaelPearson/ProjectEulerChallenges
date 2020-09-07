public class problem36 {
    public static void main(String args[]){
        int sum = 0;
        for(int i = 1; i <= 1000000; i++){
            if(checkBase2and10(i) == true){
                sum += i;
            }
        }
        System.out.println(sum);
    }
    public static boolean checkIfPalidrome(String num){
        String str = num;
        StringBuilder input = new StringBuilder();
        input.append(str);
        input = input.reverse();
        if(str.equals(input.toString())){
            return true;
        }
        return false;
    }
    public static boolean checkBase2and10(int num){

        String base2 = Integer.toBinaryString(num);
        if(checkIfPalidrome(Integer.toString(num)) == true && checkIfPalidrome(base2) == true){
            return true;
        }
        return false;
    }
}
