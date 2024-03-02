// 231RDB065 Aleksandrs Baranovskis 13

import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;

public class uzd_2_3 {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		System.out.println("231RDB065 Aleksandrs Baranovskis 13. grupa");
		
		String fileName;
		System.out.println("input file name:");
		fileName = sc.nextLine();
		sc.close();
		
        FileReader file = new FileReader(fileName);
        Scanner fileScanner = new Scanner(file);
        System.out.println("result:");
        while(sc.hasNextLine()){
            String line = fileScanner.nextLine();
            String[] lineSplit = line.split(line);

            String name = lineSplit[0];
            String surname = lineSplit[1];
            int sum = 0, count = 0, under4 = 0;
            
            for (int i = 2; i < lineSplit.length; i++){
                int grade = Integer.parseInt(lineSplit[i]);
                sum += grade;
                count++;
                if(grade < 4){
                    under4++;
                }
            }

            if((double) sum / count <= 5){
                System.out.println(name + " " + surname + " " + under4);
            }
        }
        fileScanner.close();
	}
}