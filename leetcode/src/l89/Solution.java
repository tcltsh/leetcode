package l89;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> ret = new ArrayList<Integer>();
        for(int i = 0; i < (int)Math.pow(2, n); i++){
            int grayCode = (i >> 1) ^ i;
            ret.add(grayCode);
        }
        return ret;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> ret = s.grayCode(3);
        System.out.println(ret);
    }
}
