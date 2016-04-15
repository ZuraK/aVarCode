#include <stddef.h>
#include "treegraph.h"

namespace Util
{
	BinaryTree::BinaryTree()
	{
		m_Root = NULL;
	}

	BinaryTree::~BinaryTree()
	{}

	void BinaryTree::DestroyTree(BinaryTreeNode *leaf)
	{
		if (leaf != NULL)
		{
			DestroyTree(leaf->Left);
			DestroyTree(leaf->Right);
			delete leaf;
		}
	}

	void BinaryTree::Insert(int key, BinaryTreeNode *leaf)
	{
		if (key< leaf->KeyValue)
		{
			if (leaf->Left != NULL)
				Insert(key, leaf->Left);
			else
			{
				leaf->Left = new BinaryTreeNode;
				leaf->Left->KeyValue = key;
				leaf->Left->Left = NULL;    //Sets the left child of the child node to null
				leaf->Left->Right = NULL;   //Sets the right child of the child node to null
			}
		}
		else if (key >= leaf->KeyValue)
		{
			if (leaf->Right != NULL)
				Insert(key, leaf->Right);
			else
			{
				leaf->Right = new BinaryTreeNode;
				leaf->Right->KeyValue = key;
				leaf->Right->Left = NULL;  //Sets the left child of the child node to null
				leaf->Right->Right = NULL; //Sets the right child of the child node to null
			}
		}
	}

	BinaryTreeNode *BinaryTree::Search(int key, BinaryTreeNode *leaf)
	{
		if (leaf != NULL)
		{
			if (key == leaf->KeyValue)
				return leaf;
			if (key<leaf->KeyValue)
				return search(key, leaf->Left);
			else
				return search(key, leaf->Right);
		}
		else return NULL;
	}

	void BinaryTree::Insert(int key)
	{
		if (m_Root != NULL)
			Insert(key, m_Root);
		else
		{
			m_Root = new BinaryTreeNode;
			m_Root->KeyValue = key;
			m_Root->Left = NULL;
			m_Root->Right = NULL;
		}
	}

	BinaryTreeNode *BinaryTree::Search(int key)
	{
		return Search(key, m_Root);
	}

	void BinaryTree::DestroyTree()
	{
		DestroyTree(m_Root);
	}
}
