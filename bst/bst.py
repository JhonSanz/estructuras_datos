class BST:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        self.nodes = set()
        self.head = None
        self.size = 0

    def add_recursively(self, node, ref: Node) -> None:
        if not ref.left and node < ref.value:
            new = self.Node(node)
            ref.left = new
            self.nodes.add(new)
            self.size += 1
            return
        if not ref.right and node > ref.value:
            new = self.Node(node)
            ref.right = new
            self.nodes.add(new)
            self.size += 1
            return
        if ref.left and node < ref.value:
            return self.add_recursively(node, ref.left)
        if ref.right and node > ref.value:
            return self.add_recursively(node, ref.right)

        ref.right = self.Node(node)
        self.nodes.add(new)
        self.size += 1
        return

    def bfs(self) -> list:
        queue = [self.head]
        visited = []
        while queue:
            current = queue.pop(0)
            visited.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return visited

    def dfs(self) -> list:
        stack = [self.head]
        visited = []
        while stack:
            current = stack.pop()
            visited.append(current)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return visited

    def dfs_recursively(self, nodo=None, visited=None):
        if nodo is None:
            nodo = self.head
        if visited is None:
            visited = []
        visited.append(nodo)
        if nodo.left:
            self.dfs_recursively(nodo.left, visited)
        if nodo.right:
            self.dfs_recursively(nodo.right, visited)
        return visited

    def print_bst(self, option: str) -> None:
        if option == "bfs":
            print("bfs", self.bfs())
            return
        if option == "dfs":
            print("dfs", self.dfs())
            return
        if option == "dfs_recursively":
            print("dfs_recursively", self.dfs_recursively())
            return
        print(f"{option} not available")

    def add(self, node: Node) -> None:
        if self.size == 0:
            new = self.Node(node)
            self.head = new
            self.nodes.add(new)
            self.size += 1
            return
        self.add_recursively(node, self.head)
        return


my_bst = BST()
my_bst.add(5)
my_bst.add(3)
my_bst.add(6)
my_bst.add(1)
my_bst.add(4)
my_bst.add(9)
my_bst.print_bst("bfs")
my_bst.print_bst("dfs")
my_bst.print_bst("dfs_recursively")
