#pragma once

namespace Util
{
  struct TreeNode
  {
    int KeyValue;
    TreeNode *Parent;
    std::list<TreeNode*> m_Children;
  };
  
  class Tree
  {
    public:
      Tree();
      ~Tree();
    private:
      Insert();
      Delete();
      Search();
      Clear();
  };
  
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
