def inorderTraversal_iterative(root):
    res, stack = [], []
    cur = root

    while cur or stack:          # (A) keep going while there’s work
        while cur:               # (B) descend the entire left spine
            stack.append(cur)    #     (simulate recursive calls)
            cur = cur.left

        cur = stack.pop()        # next node whose LEFT is fully done
        res.append(cur.val)      # "visit" the node
        cur = cur.right          # then do its RIGHT subtree (if any)

    return res
