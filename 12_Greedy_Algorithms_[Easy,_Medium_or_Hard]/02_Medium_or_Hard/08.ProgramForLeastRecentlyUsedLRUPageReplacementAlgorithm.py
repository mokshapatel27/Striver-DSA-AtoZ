#https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1
#LEFT

class Solution:
    def pageFaults(self, pages, c):
        
        class Solution:
        def pageFaults(self, pages, c):
            memory_set = set()
            memory_list = []
            faults = 0

            for page in pages:
                if page in memory_set:
                    # Page Hit: Move to the end (most recently used)
                    memory_list.remove(page)
                    memory_list.append(page)
                else:
                    # Page Fault
                    faults += 1
                    if len(memory_list) == c:
                        # Memory is full: Remove LRU (front of list)
                        lru_page = memory_list.pop(0)
                        memory_set.remove(lru_page)

                    # Add new page
                    memory_set.add(page)
                    memory_list.append(page)

            return faults
