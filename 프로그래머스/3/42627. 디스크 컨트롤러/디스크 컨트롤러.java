import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        // 목적 -> 작업 요청부터 종료까지 걸린 시간의 평균을 최소화해라
        // 기본적으로 '소요시간'은 무조건 들어가게 되어있다.
        // 즉, '대기시간'을 줄여야 한다.
        // 대기시간 = (작업의 실제 시작 시간 - 요청이 들어온 시간)
        // 대기시간은 다른 작업들의 '소요시간'의 합으로 이루어지게 된다 있다.

        // 작업 요청 시간과 시작시간의 간극을 최소화 하기
        
        // 하드디스크가 작업을 수행하고 있지 않을 때는 먼저 요청이 들어온 작업부터 처리한다. (큐)
        // 작업 하나가 끝났을 때, 대기시간을 줄이려면 어떤것부터 작업을 시작해야할까?
        
        // 예시 케이스를 보자.
        // 0, 3이 무조건 먼저 처리된다 (종료 시점 3초)
        // 1, 9를 넣을까 2, 6을 넣을까?
        
        // 1, 9가 먼저 들어갈 경우, 대기시간은 "2초"이고, 종료 시점은 "12초"이다.
            // 이후 2, 6을 넣을 경우, 대기시간은 "10초"이고 종료 시점은 "18초"이다.
        
        // 2, 6이 먼저 들어갈 경우, 대기시간은 "1초"이고, 종료 시점은 "9초"이다.
            // 이후 1, 9를 넣을 경우, 대기시간은 "8초"이고 종료 시점은 "15초"이다.
        
        // 즉, 요청시간이 빠른것을 먼저 처리하는게 이득으로 보인다.
        // 하지만, 요청시간이 빨라도 작업시간이 긴것을 먼저 넣게 되면, 뒤의 스케줄들이 전부 밀리므로 오히려 손해이다.
        
        // 작업을 a1, a2, a3 ... an과 같이 표기한다 했을 때,
        // 작업 ak의 대기시간은 ("현재까지 소요된 시간" - "ak의 시작시간")으로 표기할수 있다.
        
        // 즉, 작업 ak를 스케줄에 넣을 때, ak의 대기시간은 wk는 ("현재까지 완료한 작업들의 소요시간" - "ak의 시작시간")이다
        // w1, w2, w3, w4.. wn까지의 합을 최소화하는게 1차 목적이다.
        
        // '현재 시간에서 가능한 작업' 중 '가장 빠르게 끝나는 작업'을 넣어야 한다. (그리디)
        // 즉, 현재시간이 x일때 [yk, zk]가 큐에 들어갈 경우,
        // 현재시간은 x + zk로 갱신된다.
        // 다음에 들어갈 값은 x + zk >= yk 인 값 중 zk가 가장 작은 값이다
        // 그리고 결과값에는 
        
        PriorityQueue<int[]> possibleJobs = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
        PriorityQueue<int[]> jobsTimeTakes = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        for(int[] job : jobs){
            possibleJobs.add(job);
        }
        
        int answer = 0;
        int currentTime = 0;
        
        while(!possibleJobs.isEmpty() || !jobsTimeTakes.isEmpty()){
            while(!possibleJobs.isEmpty() && possibleJobs.peek()[0] <= currentTime){
                jobsTimeTakes.add(possibleJobs.poll());
            }
            
            if(!jobsTimeTakes.isEmpty()){
                int[] currentJob = jobsTimeTakes.poll();
                answer += currentTime + currentJob[1] - currentJob[0];
                currentTime += currentJob[1];
            } else {
                currentTime = possibleJobs.peek()[0];
            }
        }
        
        
        return answer / jobs.length;
    }
}