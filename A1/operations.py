import sys
import re
from supporting_modules import point,line,intersect,pp,Segment,isSameLine
from pprint import pprint

street_details={}

def add(x):
    if str(getStreetName(x).lower().strip()) in (street_details.keys()):
        print ('Error: Add Failure. Duplicate street found.')
    else:
        getRoadDetails(x)


def change(x):
    if str(getStreetName(x).lower().strip()) in (street_details.keys()):
        street_details[str(getStreetName(x)).lower().strip()] = getLocatorCoordinate(x)
    else:
        print ('Error: Cannot update item. Street not found.')


def remove(x):
    if str(getStreetName(x).lower().strip()) in (street_details.keys()):
        del street_details[str(getStreetName(x)).lower().strip()]
    else:
        print ('Error: Cannot remove item. Street not found.')


def generateGraph():
    street_segments_list = getSegmentsFromLocationCoordinates()
    vertex_value, intersection_dict = getIntesection(street_segments_list)
    vertex_value = set(vertex_value)
    vertex_list = list(vertex_value)

    vertices(vertex_list)

    list_of_edge = getEdge(vertex_list, getListFromMatrix(street_segments_list),intersection_dict)
    setofEdges(list_of_edge)


def getRoadDetails(x):
    street_details[str(getStreetName(x)).lower().strip()] = getLocatorCoordinate(x)
    return street_details
 
   
def getStreetName(x):
    x = re.search('("(.*?)"|\'(.*?)\')', x)
    name = x.group(0)
    return name[1:len(name) - 1]


def getLocatorCoordinate(x):
    find_location_coordinate = re.findall(r'(\(.*?\))', x)
    return find_location_coordinate


def getSegmentsFromLocationCoordinates():
    street_segments_list = []

    for key, values in street_details.iteritems():
        segment_list = []
        for i in range(len(values) - 1):
            x1 = values[i][1:len(values[i]) - 1]
            x2 = values[i + 1][1:len(values[i + 1]) - 1]
            x1 = re.split(',', x1)
            x2 = re.split(',', x2)
            segment = line(point(x1[0], x1[1]), point(x2[0], x2[1]))
            segment_list.append(segment)
        street_segments_list.append(segment_list)
    return street_segments_list


def getIntesection(street_segments_list):
    intersection = []
    list_intersection = []
    intersection_dict = {}
    segment_length = len(street_segments_list)
    for i in range(len(street_segments_list) - 1):
        segment_List = street_segments_list[i]
        for j in range(len(segment_List)):
            segment = segment_List[j]
            comparison_street_segment = getListFromMatrix(street_segments_list[i + 1:len(street_segments_list)])

            for k in range(len(comparison_street_segment)):
                intesection_segment = comparison_street_segment[k]
                intersect_point = intersect(segment, intesection_segment)

                if (isSameLine(intesection_segment, segment) and (intersect_point.x == 0 and intersect_point.y == 0)):
                    intersection_string = str(segment.src.x) + ',' + str(segment.src.y)
                    intersection.append(intersection_string)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = True

                    intersection_string = str(segment.dst.x) + ',' + str(segment.dst.y)
                    intersection.append(intersection_string)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = True

                    intersection_string = str(intesection_segment.src.x) + ',' + str(intesection_segment.src.y)
                    intersection.append(intersection_string)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = True

                    intersection_string = str(intesection_segment.dst.x) + ',' + str(intesection_segment.dst.y)
                    intersection.append(intersection_string)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = True

                if (not (intersect_point.x == 0 and intersect_point.y == 0)):
                    intersection_validity = Segment(intesection_segment.src, intesection_segment.dst).is_between(
                        intersect_point) and Segment(segment.src, segment.dst).is_between(intersect_point)

                    if intersection_validity:
                        intersection_string = str(intersect_point.x) + ',' + str(intersect_point.y)
                        intersection.append(intersection_string)

                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = True

                        intersection_string = str(segment.src.x) + ',' + str(segment.src.y)
                        intersection.append(intersection_string)

                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(segment.dst.x) + ',' + str(segment.dst.y)
                        intersection.append(intersection_string)

                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(intesection_segment.src.x) + ',' + str(intesection_segment.src.y)
                        intersection.append(intersection_string)

                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(intesection_segment.dst.x) + ',' + str(intesection_segment.dst.y)
                        intersection.append(intersection_string)

                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False
                    else:
                        intersection_string = str(segment.src.x) + ',' + str(segment.src.y)
                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(segment.dst.x) + ',' + str(segment.dst.y)
                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(intesection_segment.src.x) + ',' + str(intesection_segment.src.y)
                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False

                        intersection_string = str(intesection_segment.dst.x) + ',' + str(intesection_segment.dst.y)
                        if not intersection_dict.has_key(intersection_string):
                            intersection_dict[intersection_string] = False
                else:
                    intersection_string = str(segment.src.x) + ',' + str(segment.src.y)
                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = False
                    intersection_string = str(segment.dst.x) + ',' + str(segment.dst.y)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = False
                    intersection_string = str(intesection_segment.src.x) + ',' + str(intesection_segment.src.y)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = False
                    intersection_string = str(intesection_segment.dst.x) + ',' + str(intesection_segment.dst.y)

                    if not intersection_dict.has_key(intersection_string):
                        intersection_dict[intersection_string] = False
    return intersection, intersection_dict

def getListFromMatrix(streetSegments):
    list = []
    for segments in streetSegments:
        for seg in segments:
            list.append(seg)
    return list


def vertices(x):
    vertices_dictionary = {}
    n = 0
    for i in x:
        vertices_dictionary[(n + 1)] = getPointFromString(i)
        n = n + 1
    # print ('V ')
    # for key in vertices_dictionary:
    #     print str(key)+':',str(vertices_dictionary.get(key)).replace(' ','')
    # print ('}')
    count = 0
    for key in vertices_dictionary:
        count =count+1
    print ('V '+str(count-1))


    

def getPointFromString(pstring):
    cord = re.split(',', pstring)
    return point(cord[0], cord[1])


def getEdge(vertex_list, segmentList,intersection_dict):
    list_of_edge = []
    for i in range(len(vertex_list) - 1):
        point1 = getPointFromString(vertex_list[i])
        for j in range(i + 1, len(vertex_list)):
            point2 = getPointFromString(vertex_list[j])
            if getEdgeValidity(point1, point2, segmentList):
                if (intersection_dict[vertex_list[i]] or intersection_dict[vertex_list[j]]):
                    if not anyIntersectionPoint(point1, point2, intersection_dict):
                        list_of_edge.append([i + 1, j + 1])
    return list_of_edge


def anyIntersectionPoint(point1, point2, intersection_dict):
    for key, val in intersection_dict.iteritems():
        if(val):
            point = getPointFromString(key)
            if((not isSamePoint(point,point1)) and (not isSamePoint(point,point2))):
                liesBetw = Segment(point1, point2).is_between(point)
                if liesBetw:
                    return True
    return False


def isSamePoint(point1,point2):
    if(point1.x == point2.x and point1.y == point2.y):
        return True
    return False


def getEdgeValidity(point1, point2, segmentlist):
    for segment in segmentlist:
        liesBetw = Segment(segment.src, segment.dst).is_between(point1) and Segment(segment.src, segment.dst).is_between(point2)
        if liesBetw:
            return True
    return False

def setofEdges(x):
    E = set()
    for edge in x:
        x = tuple(edge)
        E.add(x)
    newlist = list(E)

    sys.stdout.write ('E {')
    for i in newlist:
        # print (newlist[i]),
        if i == newlist[-1]:
            #print (newlist[i])
            sys.stdout.write (i.__str__().replace('(', '<').replace(')', '>').replace(' ', ''))
        else:
            sys.stdout.write(i.__str__().replace('(', '<').replace(')', '>').replace(' ', '') + ',')
    print '}'
