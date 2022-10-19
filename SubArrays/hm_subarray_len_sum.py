# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.

from time import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print((end-start)*1000)
        return result
    return wrapper

@calculate_time
def solve_brute_force(A, B):
    l = len(A)
    ans = 0
    for i in range(l):
        for j in range(i, l):
            sum_of = 0
            for k in range(i,j+1):
                sum_of += A[k]
            if (sum_of < B) and (j-i+1)%2==0:
                ans += 1
            elif (sum_of > B) and (j-i+1)%2!=0:
                ans += 1
    return ans

@calculate_time
def solve_with_ps(A, B):
    #preffix sum
    ps = []
    ps.append(A[0])
    ans = 0
    for i in range(1,len(A)):
        ps.append(ps[i-1]  + A[i])
    for s in range(len(A)):
        sum_of = 0
        for e in range(s,len(A)):
            if s == 0:
                sum_of = ps[e]
            else:
                sum_of = ps[e]-ps[s-1]
            if (sum_of < B) and (e-s+1)%2==0:
                ans += 1
            elif (sum_of > B) and (e-s+1)%2!=0:
                ans += 1
    return ans




A = [1, 2, 3, 4, 5]
B = 4
# A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
# B = 65
# A = [ 514, 623, 830, 328, 892, 826, 970, 348, 118, 251, 53, 577, 616, 177, 402, 494, 58, 156, 864, 534, 1000, 192, 214, 842, 505, 605, 474, 493, 634, 940, 996, 547, 85, 232, 861, 848, 947, 182, 371, 222, 477, 76, 152, 336, 748, 638, 241, 824, 945, 814, 266, 745, 539, 854, 215, 752, 637, 806, 849, 691, 376, 511, 986, 60, 847, 177, 674, 646, 874, 68, 340, 753, 92, 775, 995, 447, 21, 148, 563, 73, 338, 134, 760, 636, 42, 898, 765, 119, 218, 758, 560, 845, 62, 404, 911, 721, 653, 780, 988, 559, 347, 491, 530, 71, 334, 829, 988, 546, 869, 434, 279, 529, 880, 176, 188, 823, 941, 455, 731, 515, 362, 580, 233, 488, 560, 426, 432, 842, 784, 966, 896, 989, 973, 27, 164, 96, 21, 730, 704, 691, 263, 226, 802, 46, 752, 105, 153, 543, 630, 656, 496, 518, 892, 545, 513, 493, 399, 215, 996, 371, 417, 656, 453, 818, 274, 273, 282, 548, 141, 678, 709, 979, 88, 516, 166, 673, 558, 12, 160, 85, 133, 307, 843, 154, 450, 669, 105, 457, 236, 160, 490, 924, 932, 410, 813, 703, 233, 715, 360, 734, 705, 287, 924, 139, 882, 587, 460, 434, 724, 302, 25, 584, 367, 55, 671, 969, 229, 892, 982, 583, 895, 584, 859, 348, 184, 798, 986, 514, 113, 915, 702, 449, 57, 472, 321, 890, 923, 404, 545, 620, 89, 234, 888, 125, 946, 5, 496, 472, 519, 442, 683, 778, 8, 410, 263, 822, 244, 696, 903, 149, 243, 63, 796, 945, 885, 809, 679, 157, 65, 684, 646, 267, 37, 221, 351, 433, 314, 289, 433, 576, 586, 334, 102, 835, 470, 214, 74, 733, 72, 471, 616, 287, 411, 695, 460, 659, 900, 546, 481, 845, 905, 79, 513, 349, 241, 555, 599, 361, 597, 44, 824, 276, 421, 68, 388, 791, 129, 22, 589, 795, 681, 849, 28, 93, 897, 868, 778, 439, 896, 943, 389, 283, 988, 621, 717, 522, 176, 102, 88, 536, 887, 81, 79, 435, 409, 257, 72, 454, 511, 838, 896, 680, 993, 525, 198, 639, 647, 299, 428, 510, 99, 695, 584, 672, 548, 66, 884, 356, 323, 637, 449, 581, 373, 188, 41, 435, 488, 815, 600, 39, 187, 68, 404, 721, 524, 75, 744, 824, 325, 363, 413, 837, 541, 968, 502, 87, 739, 511, 480, 255, 998, 298, 203, 775, 653, 553, 571, 810, 195, 667, 577, 488, 52, 673, 286, 466, 711, 1000, 85, 755, 570, 951, 978, 388, 82, 766, 899, 860, 293, 415, 500, 815, 778, 805, 919, 55, 591, 820, 465, 11, 224, 39, 173, 414, 541, 542, 733, 936, 42, 78, 264, 531, 926, 336, 27, 854, 956, 199, 712, 627, 573, 329, 793, 517, 610, 239, 918, 72, 448, 865, 126, 936, 448, 208, 347, 342, 930, 142, 231, 419, 964, 335, 647, 726, 124, 476, 761, 270, 636, 988, 772, 351, 385, 694, 291, 47, 408, 555, 699, 209, 43, 939, 801, 128, 613, 905, 149, 357, 622, 659, 797, 971, 242, 726, 952, 152, 965, 604, 336, 302, 150, 72, 254, 795, 495, 143, 322, 857, 626, 98, 560, 526, 258, 688, 531, 324, 275, 871, 645, 888, 57, 800, 580, 937, 386, 298, 159, 589, 258, 605, 217, 347, 444, 891, 174, 513, 179, 505, 760, 658, 205, 942, 807, 201, 917, 368, 331, 395, 508, 811, 260, 765, 172, 57, 414, 529, 563, 87, 189, 336, 815, 49, 829, 88, 810, 161, 768, 915, 541, 408, 774, 660, 43, 272, 151, 497, 144, 891, 538, 338, 766, 129, 695, 904, 986, 637, 208, 187, 824, 751, 500, 872, 495, 611, 877, 901, 780, 458, 817, 59, 178, 713, 11, 263, 714, 252, 691, 826, 809, 652, 990, 126, 412, 310, 191, 501, 859, 1, 230, 711, 222, 221, 738, 848, 254, 146, 698, 814, 917, 873, 579, 916, 341, 45, 699, 218, 791, 922, 669, 109, 179, 146, 586, 323, 807, 358, 145, 772, 296, 948, 267, 170, 625, 838, 894, 106, 516, 574, 464, 796, 380, 824, 342, 977, 45, 371, 74, 850, 425, 662, 892, 707, 645, 757, 377, 566, 389, 957, 479, 407, 584, 401, 524, 365, 492, 841, 620, 241, 894, 687, 761, 291, 254, 399, 477, 726, 57, 956, 566, 857, 22, 382, 640, 551, 885, 245, 521, 119, 434, 926, 902, 564, 91, 732, 307, 751, 929, 47, 327, 275, 354, 605, 198, 785, 77, 632, 860, 361, 431, 865, 822, 625, 644, 216, 553, 668, 933, 257, 814, 386, 907, 442, 940, 736, 704, 782, 508, 285, 62, 746, 346, 393, 662, 190, 440, 432, 701, 979, 394, 381, 281, 471, 979, 164, 608, 19, 570, 170, 819, 658, 486, 429, 875, 603, 580, 744, 140, 526, 15, 350, 719, 62, 6, 473, 577, 677, 632, 206, 707, 800, 448, 380, 412, 507, 565, 583, 533, 404, 89, 948, 907, 623, 57, 774, 630, 6, 776, 247, 487, 3, 936, 677, 95, 317, 238, 497, 360, 939, 933, 809, 531, 280, 487, 385, 285, 490, 529, 192, 667, 149, 962, 331, 530, 125, 752, 710, 426, 421, 803, 262, 493, 872, 95, 322, 534, 713, 872, 59, 463, 440, 195, 42, 536, 50, 900, 77, 431, 711, 4, 57, 240, 681, 145, 767, 360, 344, 954, 570, 179, 863, 557, 986, 566, 777, 436, 566, 331, 20, 136, 765, 836, 233, 280, 271, 670, 685, 929, 883, 445, 14, 119, 718, 1000, 773, 343, 91, 163, 441, 992, 579, 896, 150, 250, 214, 627, 513, 378 ]
# B = 7741965
# print("solving for good array count => " , solve_brute_force(A, B) )
print("solving for good array PS count => " , solve_with_ps(A, B) )