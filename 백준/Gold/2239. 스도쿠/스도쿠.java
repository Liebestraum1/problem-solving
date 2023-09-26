import java.util.Scanner;

public class Main {
	static boolean check = false;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[][] arr = new int[9][9];
        for (int i = 0; i < 9; i++) {
            String line = input.nextLine();
            for (int j = 0; j < 9; j++) {
                arr[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }
        sudoku(arr, 0, 0);
    }

    public static void sudoku(int[][] arr, int row, int col) {
        if(check)
        	return;
    	if (row == 9) {
            for (int[] r : arr) {
                for (int c : r) {
                    System.out.print(c);
                }
                System.out.println();
            }
            check = true;
            return;
        } else {
            if (arr[row][col] != 0) {
                sudoku(arr, row + (col + 1) / 9, (col + 1) % 9);
            } else {
                int[] can = new int[27];
                int index = 0;
                for (int i = 0; i < 9; i++) {
                    can[index++] = arr[row][i];
                    can[index++] = arr[i][col];
                }
                int startRow = row / 3 * 3;
                int startCol = col / 3 * 3;
                for (int i = startRow; i < startRow + 3; i++) {
                    for (int j = startCol; j < startCol + 3; j++) {
                        can[index++] = arr[i][j];
                    }
                }
                for (int num = 1; num <= 9; num++) {
                    boolean found = false;
                    for (int i = 0; i < can.length; i++) {
                        if (can[i] == num) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        arr[row][col] = num;
                        sudoku(arr, row + (col + 1) / 9, (col + 1) % 9);
                        arr[row][col] = 0;
                    }
                }
            }
        }
    }
}