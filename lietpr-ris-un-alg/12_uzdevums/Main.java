import java.util.Scanner;
class Main {
    static Scanner sc;
    public static int[] a;

    public static void inputArr(int i){
        if(i < a.length){
            a[i] = sc.nextInt();
            inputArr(i+1);
        }
    }

    public static int checkZero(int i){
        int res = 0;
        if(i >= 0){
            if(a[i] == 0){
                return i + 1;
            } else {
                return checkZero(i-1);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.println("231RDB065 Aleksandrs Baranovskis");
		
        int count;
		System.out.print("count: " );
        count = sc.nextInt();
        a = new int[count];
    
		System.out.println("numbers:");
        inputArr(0);
		
        System.out.print("result: ");
        System.out.print(checkZero(count-1));
    }
}