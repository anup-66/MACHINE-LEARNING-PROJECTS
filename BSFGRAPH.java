import java.util.Iterator;
import java.util.LinkedList;
public class BSFGRAPH{
    private int v;
        LinkedList<Integer> adj[];
        BSFGRAPH(int v){
            this.v = v;
            adj = new LinkedList[v];
            for(int i=0;i<v;i++){
                adj[i] = new LinkedList<>();
            }
        }
        void addToGraph(int v,int w)
        {
            adj[v].add(w);
        }
        void BFS(int s)
        {
            boolean[] visited = new boolean[v];
            
            LinkedList<Integer> queue = new LinkedList<>();
            visited[s]=true;
            queue.add(s);
            
            while(queue.size()!=0)
            {
                int n =queue.poll();
                System.out.println(n + " ");
                Iterator<Integer> i = adj[n].listIterator();
                while(i.hasNext())
                {
                    int nn  = i.next();
                    if(!visited[nn])
                    {
                        visited[nn]=true;
                        queue.add(nn);
                    }
                }
                    
                
            }
        }
    void DFSUtil(int s, boolean visited[])
    {
        // Mark the current node as visited and print it
        visited[s] = true;
        System.out.print(s + " ");
 
        // Recur for all the vertices adjacent to this
        // vertex
        Iterator<Integer> i = adj[s].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }
 
    // The function to do DFS traversal.
    // It uses recursive
    // DFSUtil()
    void DFS(int s)
    {
        // Mark all the vertices as
        // not visited(set as
        // false by default in java)
        boolean visited[] = new boolean[v];
 
        // Call the recursive helper
        // function to print DFS
        // traversal
        DFSUtil(s, visited);
    }

    
    public static void main(String[] args) {
        BSFGRAPH bg = new BSFGRAPH(7);
        bg.addToGraph(0, 1);
        bg.addToGraph(0, 2);
        bg.addToGraph(1, 3);
        bg.addToGraph(1, 4);
        bg.addToGraph(2, 5);
        bg.addToGraph(2, 6);
        long startTime = System.nanoTime();
     
        bg.BFS(0);
        long elapsedTime = System.nanoTime() - startTime;
        System.out.println((long)elapsedTime*(1/(10^8)) + " seconds");
        long startTime1 = System.nanoTime();
        bg.DFS(0);
        long elapsedTime1 = System.nanoTime() - startTime1;
        System.out.println((long)elapsedTime1*(1/(10^8)) + " seconds");
    }
}