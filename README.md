## If/Elif/Else Conditional Statements 
Used for decision-making operations with conditions

Conditional statements always start with an 
`if` header 
`elif` optional, but we can have as many as we want 
`else` optional, but only 1 for every `if` 

### Condition: 
An expression that evaluates to produce a result which is a Boolean value (AKA. Boolean expression)

### Indentation: 
Python relies on indentation to define scope in the code 

### Formula: 
if (Condition): 
> Body Statement 

elif (Condition): 
> Body Statement 

else: 
> Body Statement 

*Ex. * 
```
a = 2 
if(a == 0): # False 
  print ("hi")
else: 
  print("bye")
```  
> bye 

## Nested Conditional Statements

A conditional statement inside another conditional statement 

### Indentation 

The header/clause of a nested conditional statement must be indented from an outer header 

### Formula: 

```
if(Condition): 
  if(Condition): <-- Starting a nested statement 
    Body Statement 
  elif(Condition): 
    Body Statement 
  else: 
    Body Statement <-- End of nested statement 
elif(Condition): 
  Body Statement
else: 
  Body Statement
```

*Ex.*

```
x = 10 
y = 10 
if (x < y): 
  print("x is less than y")
else: 
  if(x > y): 
    print("x is greater than y")
  else: 
    print("x and y must be equal")
```
  > x and y must be equal