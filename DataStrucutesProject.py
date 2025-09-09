# data stracutes calasses

class HashTable:
    class HashNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self.capacity = max(1, capacity)
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = HashTable.HashNode(key, value)
            self.size += 1
            return

        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next

        current.next = HashTable.HashNode(key, value)
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        prev = None
        current = self.table[index]

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev, current = current, current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

class AVLTree:
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    # ---- utilities ----
    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # ---- rotations ----
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)
        return y

    # ---- insert ----
    def _insert(self, node, key):
        if node is None:
            return AVLTree.Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # duplicate keys not allowed

        self._update_height(node)
        balance = self._balance_factor(node)

        # balance cases
        if balance > 1 and key < node.left.key:   # LL
            return self._right_rotate(node)
        if balance > 1 and key > node.left.key:   # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key: # RR
            return self._left_rotate(node)
        if balance < -1 and key < node.right.key: # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    # ---- delete ----
    def _min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self._min_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        self._update_height(node)
        balance = self._balance_factor(node)

        # balance cases
        if balance > 1 and self._balance_factor(node.left) >= 0:   # LL
            return self._right_rotate(node)
        if balance > 1 and self._balance_factor(node.left) < 0:    # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._balance_factor(node.right) <= 0: # RR
            return self._left_rotate(node)
        if balance < -1 and self._balance_factor(node.right) > 0:  # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    # ---- traversals ----
    def inorder(self):
        def _in(node):
            if not node: return []
            return _in(node.left) + [node.key] + _in(node.right)
        return _in(self.root)

    def preorder(self):
        def _pre(node):
            if not node: return []
            return [node.key] + _pre(node.left) + _pre(node.right)
        return _pre(self.root)

    def postorder(self):
        def _post(node):
            if not node: return []
            return _post(node.left) + _post(node.right) + [node.key]
        return _post(self.root)

class Linkedlist:
    
    class ListNode:
        def __init__(self, key):
            self.key = key   
            self.next = None  
            self.previous = None
            
    def __init__(self):
        self.head = None
            
    def insert_at_front(head ,key):
            new_node = Linkedlist.ListNode(key)
            new_node.next = head
            new_node.previous = None
            return new_node
            
    def insert_at_end(head,key):
            newNode = Linkedlist.ListNode(key)
            if self.head is None:
                new_node = head

# basic classes
class Profile:
    def __init__(self,profileID,name,last_name,email):
        self.profileID = profileID
        self.name = names
        self.surname = surname
        self.email = email
        self.friends = set()
        self.posts = set()
        self.likes = set()
             
class Post:
    def __init__(self,postID,posterID,post_contant):
        self.postID = postID
        self.posterID = posterID
        self.post_contant = post_contant
        self.likersIDs = set()
        
# main functions
def quit_program():
    print("Goodbye")
    return False
    
def create_profile(): # AVL tree
    firstName = input("Name: ")
    surname = input("surname: ")
    email = input("Email: ")
    
    
    print("profile created")
    
def present_profile():  # binary search
    print("here is the profile")
    
def add_friend(): # AVL tree or hash
    print("friend added")
    
def find_friend(): # binary search
    print("the freinds of the user are:")
    
def create_post(): # hash
    posterID = input = ("Enter your user ID: ")
    post = input("Enter your post: ")
    print("new post sent")
    
def find_post(): # find in hash
    print("here is the post")
    
def like_post(): # list
    print("post liked")

# menu functions
def menu():
    commands = {
        "0": ("Exit program",quit_program),
        "1": ("Create profile", create_profile),
        "2": ("Present profile",present_profile),
        "3": ("Add freind to user",add_friend),
        "4": ("Find users friend",find_friend),
        "5": ("Create post",create_post),
        "6": ("Find users post",find_post),
        "7": ("like a post",like_post)
    }
    return commands
    
def print_menu(commands):
    print("\n==========MENU==========")
    for key,(option ,_) in commands.items():
        print(f'{key}){option}')
        
def run_menu(commands):
    while True:
        print_menu(commands)
        choice = input("\nPlease choose an option: ").strip()
        entry = commands.get(choice)
        
        if not entry:
            print("\nInvalid choice,please try again !!!")
            continue
        _ ,func = entry
        res = func()
        
        if res is False:
            break
        

def main():
    commands = menu()
    run_menu(commands)

    


if __name__ == "__main__":
    main()
