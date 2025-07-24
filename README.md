
# NFA to DFA Converter

This project implements the conversion of a Non-deterministic Finite Automaton (NFA) with epsilon (ε) transitions into a Deterministic Finite Automaton (DFA) using the ε-closure and subset construction algorithms. It is developed in **Python** as part of the **Compiler Design** course in the **5th semester** of university.



## 🔍 Project Overview

Finite Automata are fundamental in lexical analysis and compiler design. NFAs are easier to construct but harder to execute directly, while DFAs are simpler to simulate. This project automates the conversion process from NFA (possibly with ε-transitions) to an equivalent DFA.



## ⚙️ How It Works

- **ε-closure**: Computes the set of states reachable from a given set of NFA states through ε-transitions.
- **Move function**: Finds all states reachable from a set of states via a specific input symbol.
- **Subset construction algorithm**: Builds DFA states as sets of NFA states, ensuring determinism.

The input NFA is given as a set of transitions, a start state, final states, and the input alphabet. The output is a DFA represented as states and transitions with a unique start state and final states.



## 📥 Usage

1. Run the Python script.
2. Enter transitions one by one in the format:  
current\_state, input\_symbol, next\_state

3. Type `end` to finish entering transitions.
4. Enter the start state.
5. Enter the final states separated by spaces.
6. Enter the input alphabet symbols separated by spaces.

Example input:
a,e,b
a,0,a
a,1,a
b,0,c
b,1,c
c,0,c
c,1,c
end
Start state: a
Final states: c
Symbols: 0 1 e


## 💻 Requirements

- Python 3.x

## 🚀 Future Improvements

- Add GUI for interactive input and visualization.
- Extend to support regular expressions as input.
- Optimize state minimization after conversion.

## 📝 License

This project is for educational purposes and is open-source.

## 🙋‍♂️ About Me

This project was created as part of the **Compiler Design** course in the **5th semester** at university. Feel free to reach out for questions or collaboration!
