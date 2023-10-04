
public class ExcelColumnTitle {
    public static void main(String[] args) {
        Solution sol = new Solution();
        // System.out.println(sol.convertToTitle(1));
        System.out.println(sol.convertToTitle(701));
        // System.out.println(sol.convertToTitle(701));
    }
}

class Solution {

    public String convertToTitle(int columnNumber) {
        String answer = "";

        while (columnNumber > 0) {
            // because we sum number with A so we need 0 if we want to get A
            columnNumber--;

            // get the last character of the answer
            answer += ((char) (columnNumber % 26 + 'A'));
            columnNumber /= 26;
            System.out.println(columnNumber);
        }
        return new StringBuilder(answer).reverse().toString();
    }
}