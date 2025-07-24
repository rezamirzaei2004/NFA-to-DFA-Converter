
from collections import defaultdict, deque

def e_closure(states, nfa, start_states):
    stack = list(start_states)
    closure = set(start_states)

    while stack:
        state = stack.pop()
        for next_state in nfa[state].get("e", []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure


def move(states, nfa, symbol):
    accessible = {next_state for state in states for next_state in nfa[state].get(symbol, [])}
    return accessible

def nfa_to_dfa(nfa, start_state, final_states, symbols):
    dfa = {}
    queue = deque()
    visited = {}

    start_closure = frozenset(e_closure({start_state}, nfa, [start_state]))
    queue.append(start_closure)
    visited[start_closure] = 0
    dfa[0] = {"states": start_closure, "transitions": {}}

    while queue:
        current_set = queue.popleft()
        current_dfa_state = visited[current_set]

        for symbol in symbols:
            if symbol == "e":
                continue

            accessible = move(current_set, nfa, symbol)
            next_closure = frozenset(e_closure(accessible, nfa, accessible))

            if next_closure not in visited:
                new_dfa_state = len(visited)
                visited[next_closure] = new_dfa_state
                dfa[new_dfa_state] = {"states": next_closure, "transitions": {}}
                queue.append(next_closure)

            dfa[current_dfa_state]["transitions"][symbol] = visited[next_closure]

    final_states_dfa = {state_id for state_id, data in dfa.items() if any(s in final_states for s in data["states"])}

    return dfa, 0, final_states_dfa

if __name__ == "__main__":
    nfa = defaultdict(lambda: defaultdict(list))

    print("Transitions:")
    while True:
        transition = input().strip()
        if transition.lower() == "end":
            break
        state, symbol, next_state = map(str.strip, transition.split(","))
        nfa[state][symbol].append(next_state)

    start_state = input("Start state: ").strip()

    final_states = input("Final states : ").strip().split()

    symbols = input("Symbols : ").strip().split()

    dfa, start_dfa, final_states_dfa = nfa_to_dfa(nfa, start_state, final_states, symbols)

    print("\nDFA:")
    for state_id, data in dfa.items():
        state_type = "final" if state_id in final_states_dfa else "non-final"
        print(f"State {state_id} ({state_type}):")
        for symbol, next_state in data["transitions"].items():
            print(f"'{symbol}' -> State {next_state}")

    print("\nStart State:", start_dfa)
    print("Final States:", final_states_dfa)
