class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        parents={}

        for region_list in regions:
            parent=region_list[0]
            for region in region_list[1:]:
                parents[region]=parent

        ancestors=set()
        while region1:
            ancestors.add(region1)
            region1=parents.get(region1)
        
        while region2 not in ancestors:
            region2=parents.get(region2)

        return region2