states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Continue code here
def find_states_with_start_value(start_value):
    indexes = []
    [indexes.append(index) for index, value in enumerate(states) if start_value == value[0]]
    start_value_list = []
    [start_value_list.append(states[index]) for index in indexes]
    return start_value_list

M_list = find_states_with_start_value("M")
print(M_list)
W_list = find_states_with_start_value("W")
print(W_list)
V_list = find_states_with_start_value("V")
print(V_list)
