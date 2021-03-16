def schema(d, idx=0):
    """
    Print Schema of a nested Dictionary.
    """
    for k, v in d.items():
        print("\t"*idx, k)
        if isinstance(v, dict):
            schema(v, idx+1)
            

            
"""
d = {
    "Where":2,
    "to?": {
        "Help": 1,
        "Inside!": {
            "Even": 1,
            "More inside!!": 2
        }
    }
}

schema(d)
>>> 
 Where
 to?
   Help
   Inside!
     Even
     More inside!!

"""
