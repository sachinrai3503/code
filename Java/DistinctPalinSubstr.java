import java.util.HashSet;
import java.util.Iterator;

public class DistinctPalinSubstr {

    // https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/
    /**
     * Given a string of lowercase ASCII characters, find all distinct 
     * continuous palindromic sub-strings of it
     */
    void print_all_distinct_palin_substr(String str) {
        HashSet<String> set = new HashSet<String>();
        int length = str.length();
        for (int i = 0; i < length; i++) {
            int p = i, q = i;
            while (p >= 0 && q < length && str.charAt(p) == str.charAt(q)) {
                set.add(str.substring(p, q + 1));
                p--;
                q++;
            }
            p = i;
            q = i + 1;
            while (p >= 0 && q < length && str.charAt(p) == str.charAt(q)) {
                set.add(str.substring(p, q + 1));
                p--;
                q++;
            }
        }
        System.out.println("Number of distinct palindrom substr = " + 
                    set.size());
        Iterator<String> set_itr = set.iterator();
        while (set_itr.hasNext()) {
            System.out.println(set_itr.next());
        }
    }

    public static void main(String[] args) {
        String str = "aabaaa";

        DistinctPalinSubstr distinct_Palin_substr = new DistinctPalinSubstr();

        distinct_Palin_substr.print_all_distinct_palin_substr(str);
    }
}