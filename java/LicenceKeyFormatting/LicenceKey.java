package LicenceKeyFormatting;

import java.util.ArrayList;
import java.util.List;

public class LicenceKey {
    public static void main(String args[]) {
        Solution sol = new Solution();
        // System.out.println(sol.licenseKeyFormatting("5F3Z-2e-9-w-ABCD", 4));
        // System.out.println(sol.licenseKeyFormatting("2-5g-3-J", 2));

        System.out.println("n".substring(0, 1));
    }

}

class Palindrome {

    public int palindromeLength(String s, int left, int right) {
        while (left > 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public String longestPalindrome(String s) {
        int n = s.length();
        int start = 0, maxLen = 0;

        for (int i = 0; i < n; i++) {
            // Check for odd length palindromes centered at i
            int len1 = palindromeLength(s, i, i);
            // Check for even length palindromes centered between i and i+1
            int len2 = palindromeLength(s, i, i + 1);

            int len = Math.max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                // Calculate starting index based on palindrome length
                start = i - (len - 1) / 2;
            }
        }

        return s.substring(start, maxLen);
    }
}

class Solution {
    public String licenseKeyFormatting(String s, int k) {

        List<String> choppedParts = new ArrayList<String>();

        s = s.replace("-", "");
        // convert to upper case
        s = s.toUpperCase();

        if (s.length() % k == 0) {
            for (int i = 0; i < s.length(); i += k) {
                choppedParts.add(s.substring(i, i + k));
            }

        } else {
            int numberOfFirstGroup = s.length() % k;
            choppedParts.add(s.substring(0, numberOfFirstGroup));
            for (int i = numberOfFirstGroup; i < s.length(); i += k) {
                choppedParts.add(s.substring(i, i + k));
            }
        }

        return String.join("-", choppedParts);
    }

    public int longestSubstring(String s) {
        int answer = 0;

        return 0;
    }
}
