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
        return 
    

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
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
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
    def _insert(self, node, key, value=None):
        if node is None:
            return AVLTree.TreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # duplicate key: update value (common map-like behavior)
            node.value = value
            return node

        self._update_height(node)
        balance = self._balance_factor(node)

        # LL
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        # LR
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # RR
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        # RL
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    # ---- min / delete ----
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
            # node with 0 or 1 child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # node with 2 children: get inorder successor
            succ = self._min_node(node.right)
            node.key, node.value = succ.key, succ.value
            node.right = self._delete(node.right, succ.key)

        self._update_height(node)
        balance = self._balance_factor(node)

        # LL
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        # LR
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # RR
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        # RL
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    # ---- search ----
    def _get(self, node, key):
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def get(self, key):
        return self._get(self.root, key)

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
        self.name = name
        self.surname = last_name
        self.email = email
        self.friends = set()
        self.posts = set()
        self.likes = set()
        
    def __str__(self):
        return f"Profile(ID: {self.profileID}, Name: {self.name} Surname: {self.surname}, Email: {self.email})"
             
class Post:
    def __init__(self,posterID,postID,contant):
        self.posterID = posterID
        self.postID = postID
        self.post_contant = contant
        self.likersIDs = set()
        
# main functions
def quit_program():
    print("Goodbye")
    return False

tree = AVLTree()  
def create_profile(): # AVL tree

    flag = True
    while flag:
        pid=input("Pid: ").strip()
        if tree.get(pid) != None:
            print("pid exists , try again")
        else:
              flag = False
      
    firstName = input("Name: ")
    surname = input("surname: ")
    email = input("Email: ")  
    p = Profile(pid,firstName,surname,email)
    tree.insert(pid,p)
    print(f"profile created : {p}")
    
def present_profile():  # binary search
    flag1 = True
    while flag1:
        pid=input("Pid: ").strip()
        profile= tree.get(pid) 
        if profile == None:
            print("user not exist , try again")
        else:
              flag1 = False
              print("here is the profile:")
              print_profile(profile)
              
def add_friend(): # AVL tree or hash
    print("friend added")
    
def find_friend(): # binary search
    print("the freinds of the user are:")
    
post_hash = HashTable(8)
def create_post(): # hash
    pid = input("Enter the ProfileID of the user creating the post: ").strip()
    profile = does_profile_exist(pid)
    if profile is None:
        print("profile does not exist, cannot create post")
        return
    
    postID = input("Enter the PostID: ").strip() 
    if does_post_exist(postID) is not None:
        print("postID exists, try again")
        return
    
    
    contant = input("Enter the contance of your post: ")
    post = Post(pid,postID,contant)
    post_hash.insert(postID,post)
    profile.posts.add(postID)
    print("new post created")
    
def present_post(): # find in hash
    
    pid = input("ProfileID: ").strip()
    profile = does_profile_exist(pid)
    if profile is None:
        print("profile does not exist , cannot present post")
        return
    
    postID = input("PostID: ").strip()
    post = does_post_exist(postID)
    if post is None:
        print("post does not exist , cannot present post")
        return  
    
    print_post(post)
    
    
    print("here is the post")
    
def like_post(): # list
    print("post liked")

# utility functions
def does_profile_exist(pid):
    while True:
        profile = tree.get(pid)
        if profile is not None:
            return profile
        else :
            return 
        
def does_post_exist(postID):
    while True:
        post = post_hash.search(postID)
        if post is not None:
            return post
        else:
            return 
    
def print_profile(profile):
    print("--- Profile Information ---")
    print(f"ID      : {profile.profileID}")
    print(f"Name    : {profile.name} {profile.surname}")
    print(f"Email   : {profile.email}")

    # Friends
    if profile.friends:
        print("Friends:")
        for f in sorted(profile.friends):
            print(f"  - {f}")
    else:
        print("Friends: None")

    # Posts
    if profile.posts:
        print("Posts:")
        for p in sorted(profile.posts):
            print(f"  - {p}")
    else:
        print("Posts: None")

    # Likes
    if profile.likes:
        print("Likes:")
        for l in sorted(profile.likes):
            print(f"  - {l}")
    else:
        print("Likes: None")

    print("---------------------------")
    
def print_post(post):
    print("--- Post Information ---")
    print(f"Post ID      : {post.postID}")
    print(f"Posted by    : {post.posterID}")
    print(f"Content      : {post.post_contant}")

    # Likers
    if post.likersIDs:
        print("Likers:")
        for l in sorted(post.likersIDs):
            print(f"  - {l}")
    else:
        print("Likers: None")

    print("------------------------")
    
def seed_profiles():
    names = [
        "aa", "bb", "cc", "dd", "ee",
        "ff", "gg", "hh", "ii", "jj",
        "kk", "ll", "mm", "nn", "oo",
        "pp", "qq", "rr", "ss", "tt",
        "uu", "vv", "ww", "xx", "yy"
    ]

    profiles = []
    for i, name in enumerate(names, start=1):
        profiles.append(Profile(str(i), name, name, f"{name}@email.com"))

    for p in profiles:
        tree.insert(p.profileID, p)
    
# menu functions
def menu():
    commands = {
        "0": ("Exit program",quit_program),
        "1": ("Create profile", create_profile),
        "2": ("Present profile",present_profile),
        "3": ("Add freind to user",add_friend),
        "4": ("Find users friend",find_friend),
        "5": ("Create post",create_post),
        "6": ("Present post",present_post),
        "7": ("like a post",like_post)
    }
    return commands
    
def print_menu(commands):
    print("\n=========== MENU ===========")
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
    seed_profiles()
    
    commands = menu()
    run_menu(commands)
    
    

    


if __name__ == "__main__":
    main()
