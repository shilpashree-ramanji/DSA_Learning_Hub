'''
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.

A recursive algorithm takes one step toward solution and then recursively call itself to further move. The algorithm stops once we reach the solution.
Since called function may further call itself, this process might continue forever. So it is essential to provide a base case to terminate this recursion process.
Steps to Implement Recursion

Step1 - Define a base case: Identify the simplest (or base) case for which the solution is known or trivial. This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

Step2 - Define a recursive case: Define the problem in terms of smaller subproblems. Break the problem down into smaller versions of itself, and call the function recursively to solve each subproblem.

Step3 - Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case, and does not enter an infinite loop.

Step4 - Combine the solutions: Combine the solutions of the subproblems to solve the original problem.



'''

def sum(n):
    
    # base condition
    if n == 1:
        return 1
    
    return n + sum(n - 1)

if __name__ == "__main__":
    n = 5
    print(sum(n))


'''
Need of Recursion?

Recursion helps in logic building. Recursive thinking helps in solving complex problems by breaking them into smaller subproblems.
Recursive solutions work as a a basis for Dynamic Programming and Divide and Conquer algorithms.
Certain problems can be solved quite easily using recursion like Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.
What is the base condition in recursion? 
A recursive program stops at a base condition. There can be more than one base conditions in a recursion. In the above program, the base condition is when n = 1.

How a particular problem is solved using recursion? 
The idea is to represent a problem in terms of one or more smaller problems, and add one or more base conditions that stop the recursion.  



'''