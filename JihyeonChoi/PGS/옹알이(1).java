class Solution{
    public int solution(String[] babbling){
        int answer = 0;

        String pattern =  "^(aya|ye|woo|ma)+$";

        for (String word : babbling){
            if(word.matches(pattern)){
                answer++;
            }
        }return answer;
    }
}