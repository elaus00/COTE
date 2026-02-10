// 원래 풀이

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] days = new int[progresses.length];
        for (int i = 0; i < progresses.length; i++) {
            days[i] = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] != 0) {
                days[i]++;
            }
        }

        int size = 1;
        int std = days[0];

        for (int i = 1; i < progresses.length; i++) {
            if (std < days[i]) {
                size++;
                std = days[i];
            }
        }

        int[] answer = new int[size];
        answer[0] = 1;
        int idx = 0;
        std = days[0];
        for (int i = 1; i < progresses.length; i++) {
            if (std >= days[i]) {
                answer[idx]++;
            } else {
                if (idx < size) {
                    idx++;
                }
                answer[idx] = 1;
                std = days[i];
            }
        }

        return answer;
    }
}

// 개선

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();

        int n = progresses.length;
        int[] days = new int[n];

        // 1. 각 작업의 완료 일수 계산
        for (int i = 0; i < n; i++) {
            int remaining = 100 - progresses[i];
            days[i] = (remaining + speeds[i] - 1) / speeds[i];  // 올림 계산 간소화
        }

        // 2. 배포 그룹별 개수 계산 (한 번에 처리)
        int count = 1;
        int maxDay = days[0];

        for (int i = 1; i < n; i++) {
            if (maxDay >= days[i]) {
                count++;
            } else {
                result.add(count);
                count = 1;
                maxDay = days[i];
            }
        }
        result.add(count);  // 마지막 그룹 추가

        // 3. List를 배열로 변환
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
