class Solution {
    
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int failed = 0;
        int success = schedules.length;
        
        for (int i=0; i<schedules.length;i++) {
            for (int j=0; j<timelogs[i].length; j++) {
                int day = (j + startday - 1) % 7 + 1;
                
                int deadline = schedules[i] + 10;
                if (deadline % 100 >= 60) {
                    deadline = deadline + 100 - 60;
                }
                
                // 주말은 계산 안함
                if (day == 6 || day == 7) {
                    continue;
                }
                
                if (timelogs[i][j] > deadline) {
                    failed += 1;
                    break;
                }
            }   
        }
        answer = success - failed;
        
        return answer;
    }
}