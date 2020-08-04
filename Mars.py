input_value = {
    'hired': {
        'be': {
            'to': {
                'deserve': 'I'
            }
        }
    }
}

class One(object):
    def reverse(self):
        resault = {}
        for i in input_value:
            for j in input_value[i]:
                for k in input_value[i][j]:
                    for l in input_value[i][j][k]:
                        resault[input_value[i][j][k][l]] = {l:{k:{j:i}}}
        return resault

if __name__ == '__main__':
    print(One().reverse())