
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

			void Insert(int key);
			BinaryTreeNode *Search(int key);
			void DestroyTree();

		private:
			void DestroyTree(BinaryTreeNode *leaf);
			void Insert(int key, BinaryTreeNode *leaf);
			BinaryTreeNode *Search(int key, BinaryTreeNode *leaf);
			BinaryTreeNode *m_Root;
	};
}
