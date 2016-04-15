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
}
