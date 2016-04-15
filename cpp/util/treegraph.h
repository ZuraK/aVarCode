
namespace Util
{
  struct BinaryTreeNode
  {
    int KeyValue;
    BinaryTreeNode *Left;
    BinaryTreeNode *Right;
  };
  
  class BinaryTree
  {
    public:
        BinaryTree();
        ~BinaryTree();

        void insert(int key);
        BinaryTreeNode *search(int key);
        void destroy_tree();

    private:
        void destroy_tree(BinaryTreeNode *leaf);
        void insert(int key, BinaryTreeNode *leaf);
        BinaryTreeNode *search(int key, BinaryTreeNode *leaf);
        BinaryTreeNode *root;
  };
}
