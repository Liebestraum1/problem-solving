import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		Set<Integer> S = new HashSet<>();
		Set<Integer> origin = new HashSet<>();
		Set<Integer> empty = new HashSet<>();
		StringBuilder sb = new StringBuilder("");

		for (int e = 1; e < 21; e++)
			origin.add(e);

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String command = st.nextToken();

			if (!(st.hasMoreElements())) {
				if (command.equals("empty")) {
					S = new HashSet<>(empty);
				}
				if (command.equals("all")) {
					S = new HashSet<>(origin);
				}
			} else {
				int x = Integer.parseInt(st.nextToken());
				switch (command) {
				case "add": {
					S.add(x);
					break;
				}
				case "remove": {
					S.remove(x);
					break;
				}
				case "toggle": {
					if (S.contains(x))
						S.remove(x);
					else
						S.add(x);
					break;
				}
				case "check": {
					if (S.contains(x))
						sb.append("1\n");
					else
						sb.append("0\n");
					break;
				}
				}
			}
		}
		System.out.println(sb);
	}
}