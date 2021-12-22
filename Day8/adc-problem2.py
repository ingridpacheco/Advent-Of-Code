from input import input

# input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

def check_lists(five,four, seven_letters):
    new_five = [c for c in five]
    new_four = [c for c in four]
    equal = ''

    for l in five:
        if l in four and l not in seven_letters:
            equal = l
            new_four.remove(l)
            new_five.remove(l)
        if l in seven_letters:
            new_five.remove(l)

    for f in four:
        if f in seven_letters:
            new_four.remove(f)
    
    return equal, new_five[0], new_four[0]

def main():
    numbers = input.split('\n')
    final_result = 0
    numbers_mapped = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
    }

    signals = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
    }

    for n in numbers:
        result = ''
        parts = n.split(' | ')
        input_letters, output = parts[0], parts[1]
        input_letters = input_letters.split(' ')
        output = output.split(' ')

        for i in input_letters:
            if (len(i) == 2):
                numbers_mapped[1] = i
            elif (len(i) == 3):
                numbers_mapped[7] = i
            elif (len(i) == 4):
                numbers_mapped[4] = i

        for i in input_letters:
            if (len(i) == 5 and all(item in list(i) for item in list(numbers_mapped[7]))):
                seven_letters = list(numbers_mapped[7])
                five_letters = list(i)
                two_letters = list(numbers_mapped[1])
                dif_seven = list(set(seven_letters) - set(two_letters))
                signals[0] = dif_seven[0]
                four_letters = list(numbers_mapped[4])
                equal, dif_five, dif_four = check_lists(five_letters, four_letters, seven_letters)
                signals[3] = equal
                signals[6] = dif_five
                signals[1] = dif_four
                break
        
        dif_five = [signals[0], signals[1], signals[3], signals[6]]

        for i in input_letters:
            if (len(i) == 5 and all(item in list(i) for item in dif_five)):
                dif_five = list(set(list(i)) - set(dif_five))
                signals[5] = dif_five[0]
                dif_two = list(set(two_letters) - set(dif_five))
                signals[2] = dif_two[0]
                signals[4] = list(set(['a','b','c','d','e','f','g']) - set([signals[0],signals[1],signals[2],signals[3],signals[5],signals[6]]))[0]
                break

        for o in output:
            if (len(o) == 2):
                result += '1'
            elif (len(o) == 3):
                result += '7'
            elif (len(o) == 4):
                result += '4'
            elif (len(o) == 7):
                result += '8'
            elif (len(o) == 5):
                # 2,3,5
                if all(item in list(o) for item in [signals[0],signals[2],signals[3],signals[4],signals[6]]):
                    result += '2'
                elif all(item in list(o) for item in [signals[0],signals[2],signals[3],signals[5],signals[6]]):
                    result += '3'
                else:
                    result += '5'
            else:
                # 0,6,9
                if all(item in list(o) for item in [signals[0],signals[1],signals[2],signals[4],signals[5],signals[6]]):
                    result += '0'
                elif all(item in list(o) for item in [signals[0],signals[1],signals[3],signals[4],signals[5],signals[6]]):
                    result += '6'
                else:
                    result += '9'
        
        signals = {
            0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
        }

        numbers_mapped = {
            0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: '',
        }
        print(result)

        final_result += int(result)

    return final_result

if __name__ == "__main__":
    print(main())