import java.util.*;

class Ticket{
    String destination;
    boolean isUsed;
    
    Ticket(String destination, boolean isUsed){
        this.destination = destination;
        this.isUsed = isUsed;
    }
}

class Solution {
    List<List<String>> answers = new ArrayList<>();
    
    public void dfs(
        int ticketAmount,
        Map<String, List<Ticket>> graph,
        List<String> answer,
        String departure
    ){
        if(ticketAmount == 0){
            answers.add(new ArrayList<>(answer));
            return;
        }
        
        if(!graph.containsKey(departure)){
            return;
        }
        
        for(Ticket ticket : graph.get(departure)){
            if(!ticket.isUsed){
                answer.add(ticket.destination);
                ticket.isUsed = true;
                
                dfs(ticketAmount - 1, graph, answer, ticket.destination);
                
                ticket.isUsed = false;
                answer.remove(answer.size() - 1);
            }
        }
    }
    
    public String[] solution(String[][] tickets) {
        Map<String, List<Ticket>> graph = new HashMap<>();
        int ticketAmount = 0;

        for(String[] ticketInfo : tickets) {
            String departure = ticketInfo[0];
            Ticket ticket = new Ticket(ticketInfo[1], false);
            
            if(!graph.containsKey(departure)){
                graph.put(departure, new ArrayList<>());
            }

            graph.get(departure).add(ticket);
            ticketAmount += 1;
        }

        for(String key : graph.keySet()){
            graph.get(key).sort(((o1, o2) -> o1.destination.compareTo(o2.destination)));
        }
        
        dfs(ticketAmount, graph, new ArrayList<String>(List.of("ICN")), "ICN");
        
        return answers.get(0).toArray(new String[0]);
    }
}