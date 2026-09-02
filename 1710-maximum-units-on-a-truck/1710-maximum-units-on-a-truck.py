class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        units = 0

        for boxes, unit in boxTypes:
            if boxes <= truckSize:
                units += boxes * unit
                truckSize -= boxes
            else:
                units += truckSize * unit
                break

        return units