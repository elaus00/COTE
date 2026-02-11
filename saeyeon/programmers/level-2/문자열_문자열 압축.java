class Solution {
    public int solution(String s) {
        int minLength = s.length(); // 압축 x
        for (int unit = 1; unit <= s.length() / 2; unit++; {
            String compressed = compress(s, unit);
            minLength = Math.min(minLength, compressed.length)
        }

        return minLength;
    }

    private String compress(String s, int unit) {
        StringBuilder sb = new StringBuilder();
        String prev = s.substring(0, unit);
        int count = 1;

        for (int i = unit; i < s.length(); i += unit) {
            int end = Math.min(i + unit, s.length());
            String current = s.substring(i, end));
            String current = s.substring(i, end);

            if (prev.equals(current)) {
                count++;
            } else {
                if (count > 1) { sb.append(count); }
                sb.append(prev);
            }
        }
        return sb.toString();
    }
}