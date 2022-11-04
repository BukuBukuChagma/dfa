class DFA:
    def __init__(self, alpha, states, start_state, final_states, transition_table):
        self.alphabets = alpha
        self.states = states
        self.start_state = start_state
        self.final_states = final_states
        self.transition_table = transition_table
    
    def transition(self, letter, state):
        return self.transition_table[(state, letter)]

    def run(self, string):
        current_state = self.start_state
        if len(string) == 0 and current_state in final_states:
            return "Accepted"
        else:
            for str in string:
                if str in self.alphabets:
                    current_state = self.transition(str, current_state)
                else:
                    return "Invalid String!! Letter not in Alphabets!"

            if current_state in self.final_states:
                return "Accepted"
            else:
                return "Rejected"


#DFA 1
alphabets = ['0', '1']
states = ['q0', 'q1', 'q2', 'q3']
start_state = 'q0'
final_states = ['q0']

transition_table = {('q0', '0'): 'q1', ('q0', '1'): 'q3', ('q1', '0'): 'q0', ('q1', '1'): 'q2', ('q2', '0'): 'q3', ('q2', '1'): 'q1', ('q3', '0'): 'q2', ('q3', '1'): 'q0'}

dfa1 = DFA(alpha=alphabets, states=states, start_state=start_state, final_states=final_states, transition_table=transition_table)


#DFA 2

alphabets = ['0', '1']
states = ['q0', 'q1', 'q2', 'q3' 'q4']
start_state = 'q0'
final_states = ['q2', 'q4']

transition_table = {('q0', '0'): 'q3', ('q0', '1'): 'q1', ('q1', '0'): 'q1', ('q1', '1'): 'q2', ('q2', '0'): 'q2', ('q2', '1'): 'q2', ('q3', '0'): 'q4', ('q3', '1'): 'q3', ('q4', '0'): 'q4', ('q4', '1'): 'q4'}

dfa2 = DFA(alpha=alphabets, states=states, start_state=start_state, final_states=final_states, transition_table=transition_table)


#DFA 3

alphabets = ['a', 'b', 'c']
states = ['q0', 'q1', 'q2', 'q3']
start_state = 'q0'
final_states = ['q2']

transition_table = {('q0', 'a'): 'q2', ('q0', 'b'): 'q2', ('q0', 'c'): 'q1', ('q1', 'a'): 'q3', ('q1', 'b'): 'q2', ('q1', 'c'): 'q2', ('q2', 'a'): 'q3', ('q2', 'b'): 'q3', ('q2', 'c'): 'q3', ('q3', 'a'): 'q3', ('q3', 'b'): 'q3', ('q3', 'c'): 'q3'}

dfa3 = DFA(alpha=alphabets, states=states, start_state=start_state, final_states=final_states, transition_table=transition_table)


#Running all dfa
string_dfa1 = '0011'
print(dfa1.run(string_dfa1))

string_dfa2 = '0111'
print(dfa2.run(string_dfa2))

string_dfa3 = 'cb'
print(dfa3.run(string_dfa3))