# -*- coding: utf-8 -*-

# This code was created without modifications from the JS version.


def v(person, choices, w, r):
    sum = 0
    if choices[62] == 1:
        sum += 1
    if choices[90] == 1:
        sum += 1
    if choices[152] == 1:
        sum += 1
    if choices[169] == 1:
        sum += 1
    w[25] = sum
    r[25] = "Validity"
    return sum


def pp(person, choices, w, r):
    sum = 0
    if choices[15] == 1:
        sum += 1
    if choices[16] == 1:
        sum += 2
    if choices[24] == 1:
        sum += 2
    if choices[32] == 1:
        sum += 1
    if choices[38] == 1:
        sum += 2
    if choices[39] == 1:
        sum += 1
    if choices[69] == 1:
        sum += 2
    if choices[74] == 1:
        sum += 1
    if choices[80] == 1:
        sum += 3
    if choices[84] == 1:
        sum += 2
    if choices[85] == 1:
        sum += 2
    if choices[89] == 1:
        sum += 1
    if choices[98] == 1:
        sum += 2
    if choices[100] == 1:
        sum += 3
    if choices[112] == 1:
        sum += 1
    if choices[123] == 1:
        sum += 3
    if choices[126] == 1:
        sum += 1
    if choices[131] == 1:
        sum += 2
    if choices[138] == 1:
        sum += 1
    if choices[143] == 1:
        sum += 1
    if choices[146] == 1:
        sum += 2
    if choices[164] == 1:
        sum += 2
    if (sum > 36):
        sum = 36
    r[24] = "Delusional disorder"
    w[24] = sum
    return sum


def cc(person, choices, w, r):
    sum = 0
    if choices[5] == 1:
        sum += 3
    if choices[19] == 1:
        sum += 1
    if choices[26] == 1:
        sum += 3
    if choices[33] == 1:
        sum += 2
    if choices[36] == 1:
        sum += 3
    if choices[45] == 1:
        sum += 2
    if choices[47] == 1:
        sum += 2
    if choices[50] == 1:
        sum += 2
    if choices[51] == 1:
        sum += 1
    if choices[53] == 1:
        sum += 3
    if choices[54] == 1:
        sum += 1
    if choices[56] == 1:
        sum += 2
    if choices[57] == 1:
        sum += 1
    if choices[58] == 1:
        sum += 1
    if choices[59] == 1:
        sum += 3
    if choices[65] == 1:
        sum += 1
    if choices[67] == 1:
        sum += 1
    if choices[72] == 1:
        sum += 2
    if choices[76] == 1:
        sum += 3
    if choices[79] == 1:
        sum += 2
    if choices[81] == 1:
        sum += 1
    if choices[82] == 1:
        sum += 1
    if choices[95] == 1:
        sum += 1
    if choices[96] == 1:
        sum += 2
    if choices[99] == 1:
        sum += 1
    if choices[108] == 1:
        sum += 2
    if choices[109] == 1:
        sum += 2
    if choices[110] == 1:
        sum += 1
    if choices[117] == 1:
        sum += 1
    if choices[136] == 1:
        sum += 3
    if choices[154] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 46):
            sum = 46
        elif (sum > 48):
            sum = 48
    r[23] = "Major Depression"
    w[23] = sum
    return sum


def ss(person, choices, w, r):
    sum = 0
    if choices[3] == 1:
        sum += 1
    if choices[8] == 1:
        sum += 1
    if choices[13] == 1:
        sum += 1
    if choices[19] == 1:
        sum += 1
    if choices[23] == 1:
        sum += 1
    if choices[24] == 1:
        sum += 1
    if choices[29] == 1:
        sum += 1
    if choices[31] == 1:
        sum += 1
    if choices[38] == 1:
        sum += 2
    if choices[68] == 1:
        sum += 2
    if choices[69] == 1:
        sum += 2
    if choices[74] == 1:
        sum += 1
    if choices[77] == 1:
        sum += 2
    if choices[80] == 1:
        sum += 2
    if choices[82] == 1:
        sum += 1
    if choices[83] == 1:
        sum += 2
    if choices[85] == 1:
        sum += 2
    if choices[98] == 1:
        sum += 3
    if choices[102] == 1:
        sum += 2
    if choices[109] == 1:
        sum += 3
    if choices[112] == 1:
        sum += 2
    if choices[115] == 1:
        sum += 2
    if choices[120] == 1:
        sum += 2
    if choices[124] == 1:
        sum += 3
    if choices[127] == 1:
        sum += 3
    if choices[141] == 1:
        sum += 1
    if choices[146] == 1:
        sum += 2
    if choices[147] == 1:
        sum += 1
    if choices[156] == 1:
        sum += 1
    if choices[160] == 1:
        sum += 3
    if choices[161] == 1:
        sum += 1
    if choices[164] == 1:
        sum += 2
    if choices[167] == 1:
        sum += 3
    if person.sex == 0:
        if (sum > 39):
            sum = 39
        elif (sum > 47):
            sum = 47
    r[22] = "Thought Disorder"
    w[22] = sum
    return sum


def t(person, choices, w, r):
    sum = 0
    if choices[1] == 1:
        sum += 2
    if choices[6] == 1:
        sum += 1
    if choices[7] == 1:
        sum += 2
    if choices[9] == 1:
        sum += 2
    if choices[12] == 1:
        sum += 1
    if choices[14] == 1:
        sum += 1
    if choices[20] == 1:
        sum += 2
    if choices[22] == 1:
        sum += 2
    if choices[30] == 1:
        sum += 1
    if choices[32] == 1:
        sum += 1
    if choices[35] == 1:
        sum += 3
    if choices[40] == 1:
        sum += 2
    if choices[43] == 1:
        sum += 2
    if choices[44] == 1:
        sum += 1
    if choices[50] == 1:
        sum += 1
    if choices[55] == 1:
        sum += 1
    if choices[58] == 1:
        sum += 2
    if choices[60] == 1:
        sum += 1
    if choices[61] == 2:
        sum += 1
    if choices[66] == 1:
        sum += 1
    if choices[70] == 1:
        sum += 3
    if choices[73] == 1:
        sum += 2
    if choices[80] == 1:
        sum += 2
    if choices[82] == 1:
        sum += 2
    if choices[86] == 1:
        sum += 2
    if choices[89] == 1:
        sum += 1
    if choices[91] == 1:
        sum += 2
    if choices[92] == 1:
        sum += 2
    if choices[93] == 1:
        sum += 1
    if choices[94] == 1:
        sum += 1
    if choices[95] == 1:
        sum += 2
    if choices[101] == 1:
        sum += 1
    if choices[103] == 1:
        sum += 2
    if choices[104] == 1:
        sum += 1
    if choices[105] == 1:
        sum += 3
    if choices[111] == 1:
        sum += 1
    if choices[113] == 1:
        sum += 1
    if choices[114] == 1:
        sum += 1
    if choices[115] == 1:
        sum += 2
    if choices[116] == 1:
        sum += 1
    if choices[117] == 1:
        sum += 2
    if choices[120] == 1:
        sum += 1
    if choices[123] == 1:
        sum += 1
    if choices[125] == 1:
        sum += 1
    if choices[128] == 1:
        sum += 1
    if choices[129] == 1:
        sum += 2
    if choices[130] == 1:
        sum += 1
    if choices[137] == 1:
        sum += 1
    if choices[140] == 1:
        sum += 3
    if choices[144] == 1:
        sum += 3
    if choices[146] == 1:
        sum += 1
    if choices[155] == 1:
        sum += 1
    if choices[162] == 1:
        sum += 2
    if choices[165] == 1:
        sum += 1
    if choices[166] == 1:
        sum += 1
    if choices[171] == 1:
        sum += 1
    if choices[172] == 1:
        sum += 1
    if choices[175] == 1:
        sum += 3
    if person.sex == 0:
        if (sum > 60):
            sum = 60
        elif (sum > 63):
            sum = 63
    r[21] = "Drug dependence"
    w[21] = sum
    return sum


def b(person, choices, w, r):
    sum = 0
    if choices[8] == 2:
        sum += 1
    if choices[17] == 1:
        sum += 3
    if choices[18] == 1:
        sum += 2
    if choices[22] == 1:
        sum += 1
    if choices[23] == 1:
        sum += 1
    if choices[25] == 1:
        sum += 1
    if choices[27] == 1:
        sum += 1
    if choices[35] == 1:
        sum += 1
    if choices[40] == 1:
        sum += 1
    if choices[46] == 1:
        sum += 1
    if choices[52] == 2:
        sum += 2
    if choices[54] == 1:
        sum += 2
    if choices[65] == 1:
        sum += 1
    if choices[70] == 1:
        sum += 1
    if choices[73] == 1:
        sum += 2
    if choices[80] == 1:
        sum += 1
    if choices[87] == 1:
        sum += 3
    if choices[93] == 1:
        sum += 1
    if choices[95] == 1:
        sum += 2
    if choices[96] == 1:
        sum += 1
    if choices[97] == 1:
        sum += 2
    if choices[103] == 1:
        sum += 1
    if choices[104] == 1:
        sum += 1
    if choices[105] == 1:
        sum += 2
    if choices[108] == 1:
        sum += 1
    if choices[109] == 1:
        sum += 2
    if choices[111] == 1:
        sum += 1
    if choices[114] == 1:
        sum += 1
    if choices[117] == 1:
        sum += 1
    if choices[119] == 1:
        sum += 3
    if choices[122] == 2:
        sum += 2
    if choices[125] == 1:
        sum += 1
    if choices[128] == 1:
        sum += 1
    if choices[130] == 1:
        sum += 1
    if choices[135] == 1:
        sum += 1
    if choices[137] == 1:
        sum += 1
    if choices[140] == 1:
        sum += 1
    if choices[144] == 1:
        sum += 2
    if choices[149] == 1:
        sum += 1
    if choices[155] == 1:
        sum += 1
    if choices[157] == 1:
        sum += 3
    if choices[159] == 1:
        sum += 1
    if choices[162] == 1:
        sum += 1
    if choices[165] == 1:
        sum += 1
    if choices[171] == 1:
        sum += 1
    if choices[175] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 51):
            sum = 51
        elif (sum > 50):
            sum = 50
    w[20] = sum
    r[20] = "Alcohol dependence"
    return sum


def d(person, choices, w, r):
    sum = 0
    if choices[5] == 1:
        sum += 2
    if choices[8] == 1:
        sum += 2
    if choices[25] == 1:
        sum += 1
    if choices[26] == 1:
        sum += 2
    if choices[27] == 1:
        sum += 3
    if choices[36] == 1:
        sum += 2
    if choices[41] == 2:
        sum += 1
    if choices[45] == 1:
        sum += 3
    if choices[46] == 1:
        sum += 1
    if choices[51] == 1:
        sum += 2
    if choices[53] == 1:
        sum += 2
    if choices[54] == 1:
        sum += 3
    if choices[56] == 1:
        sum += 1
    if choices[59] == 1:
        sum += 2
    if choices[65] == 1:
        sum += 2
    if choices[71] == 1:
        sum += 2
    if choices[72] == 1:
        sum += 2
    if choices[76] == 1:
        sum += 2
    if choices[79] == 1:
        sum += 3
    if choices[83] == 1:
        sum += 2
    if choices[86] == 2:
        sum += 1
    if choices[96] == 1:
        sum += 2
    if choices[97] == 1:
        sum += 3
    if choices[99] == 1:
        sum += 3
    if choices[107] == 1:
        sum += 1
    if choices[108] == 1:
        sum += 3
    if choices[109] == 1:
        sum += 2
    if choices[110] == 1:
        sum += 1
    if choices[132] == 1:
        sum += 3
    if choices[136] == 1:
        sum += 2
    if choices[139] == 1:
        sum += 1
    if choices[154] == 1:
        sum += 2
    if choices[155] == 1:
        sum += 1
    if choices[166] == 2:
        sum += 2
    if choices[167] == 1:
        sum += 1
    if choices[168] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 56):
            sum = 56
        elif (sum > 57):
            sum = 57
    w[19] = sum
    r[19] = "Dysthymia"
    return sum


def n(person, choices, w, r):
    sum = 0
    if choices[11] == 1:
        sum += 3
    if choices[14] == 1:
        sum += 2
    if choices[17] == 1:
        sum += 1
    if choices[19] == 2:
        sum += 1
    if choices[20] == 1:
        sum += 2
    if choices[28] == 1:
        sum += 2
    if choices[37] == 1:
        sum += 1
    if choices[40] == 1:
        sum += 1
    if choices[42] == 2:
        sum += 1
    if choices[50] == 1:
        sum += 2
    if choices[58] == 1:
        sum += 1
    if choices[60] == 1:
        sum += 2
    if choices[66] == 1:
        sum += 1
    if choices[67] == 1:
        sum += 1
    if choices[73] == 1:
        sum += 1
    if choices[86] == 1:
        sum += 2
    if choices[89] == 1:
        sum += 1
    if choices[93] == 1:
        sum += 3
    if choices[95] == 1:
        sum += 1
    if choices[98] == 1:
        sum += 1
    if choices[101] == 1:
        sum += 1
    if choices[103] == 1:
        sum += 2
    if choices[111] == 1:
        sum += 1
    if choices[121] == 1:
        sum += 1
    if choices[125] == 1:
        sum += 2
    if choices[127] == 1:
        sum += 1
    if choices[128] == 1:
        sum += 2
    if choices[131] == 1:
        sum += 1
    if choices[134] == 1:
        sum += 2
    if choices[137] == 1:
        sum += 2
    if choices[151] == 1:
        sum += 3
    if choices[158] == 2:
        sum += 1
    if choices[161] == 2:
        sum += 1
    if choices[166] == 1:
        sum += 1
    if choices[170] == 1:
        sum += 2
    if choices[172] == 1:
        sum += 1
    if choices[174] == 1:
        sum += 3
    if person.sex == 0:
        if (sum > 44):
            sum = 44
        elif(sum > 45):
            sum = 45
    w[18] = sum
    r[18] = "Bipolar:Manic"
    return sum


def h(person, choices, w, r):
    sum = 0
    if choices[5] == 1:
        sum += 1
    if choices[18] == 1:
        sum += 2
    if choices[26] == 1:
        sum += 1
    if choices[29] == 1:
        sum += 3
    if choices[31] == 1:
        sum += 1
    if choices[33] == 1:
        sum += 3
    if choices[36] == 1:
        sum += 1
    if choices[41] == 2:
        sum += 1
    if choices[42] == 1:
        sum += 1
    if choices[50] == 1:
        sum += 1
    if choices[51] == 1:
        sum += 2
    if choices[53] == 1:
        sum += 2
    if choices[56] == 1:
        sum += 1
    if choices[60] == 1:
        sum += 1
    if choices[66] == 1:
        sum += 1
    if choices[67] == 1:
        sum += 2
    if choices[68] == 1:
        sum += 3
    if choices[71] == 1:
        sum += 3
    if choices[72] == 1:
        sum += 3
    if choices[78] == 1:
        sum += 1
    if choices[96] == 1:
        sum += 3
    if choices[98] == 1:
        sum += 2
    if choices[102] == 1:
        sum += 1
    if choices[109] == 1:
        sum += 1
    if choices[114] == 1:
        sum += 2
    if choices[117] == 1:
        sum += 1
    if choices[118] == 1:
        sum += 1
    if choices[137] == 1:
        sum += 1
    if choices[145] == 1:
        sum += 1
    if choices[170] == 1:
        sum += 1
    if choices[173] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 43):
            sum = 43
        elif(sum > 44):
            sum = 44
    w[17] = sum
    r[17] = "Somatoform"
    return sum


def a(person, choices, w, r):
    sum = 0
    if choices[8] == 1:
        sum += 1
    if choices[16] == 1:
        sum += 1
    if choices[18] == 1:
        sum += 3
    if choices[26] == 1:
        sum += 1
    if choices[29] == 1:
        sum += 2
    if choices[33] == 1:
        sum += 2
    if choices[36] == 1:
        sum += 1
    if choices[51] == 1:
        sum += 3
    if choices[53] == 1:
        sum += 2
    if choices[54] == 1:
        sum += 1
    if choices[67] == 1:
        sum += 3
    if choices[71] == 1:
        sum += 2
    if choices[78] == 1:
        sum += 1
    if choices[96] == 1:
        sum += 2
    if choices[97] == 1:
        sum += 2
    if choices[99] == 1:
        sum += 1
    if choices[108] == 1:
        sum += 1
    if choices[109] == 1:
        sum += 2
    if choices[114] == 1:
        sum += 3
    if choices[117] == 1:
        sum += 3
    if choices[132] == 1:
        sum += 1
    if choices[145] == 1:
        sum += 1
    if choices[153] == 1:
        sum += 1
    if choices[166] == 2:
        sum += 1
    if choices[167] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 36):
            sum = 36
        elif (sum > 39):
            sum = 39
    w[16] = sum
    r[16] = "Anxiety"
    return sum


def p(person, choices, w, r):
    sum = 0
    if choices[6] == 1:
        sum += 1
    if choices[12] == 1:
        sum += 1
    if choices[15] == 1:
        sum += 2
    if choices[16] == 1:
        sum += 3
    if choices[21] == 1:
        sum += 1
    if choices[22] == 1:
        sum += 1
    if choices[24] == 1:
        sum += 2
    if choices[30] == 1:
        sum += 1
    if choices[32] == 1:
        sum += 3
    if choices[37] == 1:
        sum += 2
    if choices[38] == 1:
        sum += 3
    if choices[39] == 1:
        sum += 1
    if choices[41] == 1:
        sum += 1
    if choices[43] == 1:
        sum += 1
    if choices[44] == 1:
        sum += 1
    if choices[46] == 1:
        sum += 2
    if choices[55] == 1:
        sum += 1
    if choices[61] == 1:
        sum += 1
    if choices[63] == 1:
        sum += 1
    if choices[64] == 1:
        sum += 3
    if choices[68] == 1:
        sum += 1
    if choices[74] == 1:
        sum += 3
    if choices[75] == 1:
        sum += 1
    if choices[80] == 1:
        sum += 2
    if choices[84] == 1:
        sum += 3
    if choices[85] == 1:
        sum += 3
    if choices[89] == 1:
        sum += 2
    if choices[98] == 1:
        sum += 1
    if choices[100] == 1:
        sum += 2
    if choices[103] == 1:
        sum += 2
    if choices[123] == 1:
        sum += 2
    if choices[126] == 1:
        sum += 2
    if choices[127] == 1:
        sum += 1
    if choices[129] == 1:
        sum += 2
    if choices[131] == 1:
        sum += 2
    if choices[135] == 1:
        sum += 1
    if choices[138] == 1:
        sum += 1
    if choices[143] == 1:
        sum += 1
    if choices[146] == 1:
        sum += 3
    if choices[163] == 1:
        sum += 1
    if choices[164] == 1:
        sum += 3
    if choices[165] == 1:
        sum += 1
    if choices[171] == 1:
        sum += 1
    if choices[172] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 62):
            sum = 62
        elif (sum > 59):
            sum = 59
    w[15] = sum
    r[15] = "Paranoid"
    return sum


def c(person, choices, w, r):
    sum = 0
    if choices[5] == 1:
        sum += 2
    if choices[7] == 1:
        sum += 1
    if choices[22] == 1:
        sum += 2
    if choices[23] == 1:
        sum += 2
    if choices[25] == 1:
        sum += 3
    if choices[26] == 1:
        sum += 2
    if choices[27] == 1:
        sum += 2
    if choices[35] == 1:
        sum += 2
    if choices[36] == 1:
        sum += 1
    if choices[40] == 1:
        sum += 1
    if choices[43] == 1:
        sum += 3
    if choices[44] == 1:
        sum += 1
    if choices[50] == 1:
        sum += 2
    if choices[51] == 1:
        sum += 1
    if choices[53] == 1:
        sum += 1
    if choices[54] == 1:
        sum += 1
    if choices[56] == 1:
        sum += 3
    if choices[57] == 1:
        sum += 1
    if choices[58] == 1:
        sum += 3
    if choices[59] == 1:
        sum += 2
    if choices[65] == 1:
        sum += 1
    if choices[66] == 1:
        sum += 2
    if choices[67] == 1:
        sum += 1
    if choices[72] == 1:
        sum += 1
    if choices[73] == 1:
        sum += 3
    if choices[74] == 1:
        sum += 1
    if choices[77] == 1:
        sum += 1
    if choices[78] == 1:
        sum += 1
    if choices[79] == 1:
        sum += 2
    if choices[82] == 1:
        sum += 3
    if choices[91] == 1:
        sum += 2
    if choices[94] == 1:
        sum += 1
    if choices[95] == 1:
        sum += 2
    if choices[97] == 1:
        sum += 2
    if choices[99] == 1:
        sum += 1
    if choices[101] == 1:
        sum += 2
    if choices[103] == 1:
        sum += 1
    if choices[104] == 1:
        sum += 1
    if choices[108] == 1:
        sum += 1
    if choices[110] == 1:
        sum += 1
    if choices[113] == 1:
        sum += 3
    if choices[115] == 1:
        sum += 3
    if choices[128] == 1:
        sum += 3
    if choices[129] == 1:
        sum += 2
    if choices[130] == 1:
        sum += 1
    if choices[132] == 1:
        sum += 1
    if choices[135] == 1:
        sum += 1
    if choices[136] == 1:
        sum += 2
    if choices[139] == 1:
        sum += 1
    if choices[140] == 1:
        sum += 2
    if choices[142] == 1:
        sum += 2
    if choices[144] == 1:
        sum += 1
    if choices[147] == 1:
        sum += 1
    if choices[154] == 1:
        sum += 1
    if choices[155] == 1:
        sum += 3
    if choices[156] == 1:
        sum += 2
    if choices[162] == 1:
        sum += 1
    if choices[165] == 1:
        sum += 1
    if choices[167] == 1:
        sum += 1
    if choices[168] == 1:
        sum += 1
    if choices[171] == 1:
        sum += 3
    if choices[173] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 64):
            sum = 64
        elif (sum > 65):
            sum = 65
    w[14] = sum
    r[14] = "Borderline"
    return sum


def s(person, choices, w, r):
    sum = 0
    if choices[2] == 1:
        sum += 2
    if choices[3] == 1:
        sum += 2
    if choices[8] == 1:
        sum += 2
    if choices[10] == 1:
        sum += 1
    if choices[13] == 1:
        sum += 1
    if choices[14] == 2:
        sum += 1
    if choices[19] == 1:
        sum += 1
    if choices[23] == 1:
        sum += 1
    if choices[24] == 1:
        sum += 3
    if choices[25] == 1:
        sum += 1
    if choices[31] == 1:
        sum += 2
    if choices[38] == 1:
        sum += 2
    if choices[47] == 1:
        sum += 3
    if choices[48] == 2:
        sum += 1
    if choices[49] == 1:
        sum += 2
    if choices[53] == 1:
        sum += 1
    if choices[60] == 2:
        sum += 1
    if choices[63] == 1:
        sum += 2
    if choices[69] == 1:
        sum += 3
    if choices[77] == 1:
        sum += 2
    if choices[83] == 1:
        sum += 3
    if choices[85] == 1:
        sum += 2
    if choices[100] == 1:
        sum += 2
    if choices[102] == 1:
        sum += 3
    if choices[108] == 1:
        sum += 1
    if choices[112] == 1:
        sum += 3
    if choices[113] == 1:
        sum += 2
    if choices[118] == 1:
        sum += 3
    if choices[120] == 1:
        sum += 2
    if choices[123] == 1:
        sum += 2
    if choices[124] == 1:
        sum += 2
    if choices[130] == 1:
        sum += 1
    if choices[133] == 1:
        sum += 2
    if choices[136] == 1:
        sum += 1
    if choices[141] == 1:
        sum += 2
    if choices[147] == 1:
        sum += 1
    if choices[150] == 1:
        sum += 3
    if choices[158] == 1:
        sum += 2
    if choices[160] == 1:
        sum += 1
    if choices[161] == 1:
        sum += 1
    if choices[162] == 1:
        sum += 1
    if choices[164] == 1:
        sum += 2
    if choices[165] == 1:
        sum += 1
    if choices[166] == 2:
        sum += 2
    if (sum > 48):
        sum = 48
    w[13] = sum
    r[13] = "Schizotypal"
    return sum


def eightb(person, choices, w, r):
    sum = 0
    if choices[8] == 1:
        sum += 1
    if choices[10] == 1:
        sum += 2
    if choices[16] == 1:
        sum += 2
    if choices[18] == 1:
        sum += 1
    if choices[23] == 1:
        sum += 3
    if choices[25] == 1:
        sum += 1
    if choices[28] == 1:
        sum += 2
    if choices[31] == 1:
        sum += 1
    if choices[42] == 1:
        sum += 2
    if choices[45] == 1:
        sum += 2
    if choices[51] == 1:
        sum += 2
    if choices[54] == 1:
        sum += 2
    if choices[56] == 1:
        sum += 2
    if choices[57] == 1:
        sum += 3
    if choices[63] == 1:
        sum += 1
    if choices[65] == 1:
        sum += 3
    if choices[71] == 1:
        sum += 1
    if choices[73] == 1:
        sum += 1
    if choices[74] == 2:
        sum += 1
    if choices[77] == 1:
        sum += 2
    if choices[81] == 1:
        sum += 1
    if choices[82] == 1:
        sum += 1
    if choices[99] == 1:
        sum += 1
    if choices[106] == 1:
        sum += 2
    if choices[110] == 1:
        sum += 3
    if choices[115] == 1:
        sum += 2
    if choices[120] == 1:
        sum += 2
    if choices[121] == 1:
        sum += 3
    if choices[128] == 1:
        sum += 1
    if choices[132] == 1:
        sum += 2
    if choices[133] == 1:
        sum += 1
    if choices[139] == 1:
        sum += 3
    if choices[141] == 1:
        sum += 1
    if choices[145] == 1:
        sum += 2
    if choices[154] == 1:
        sum += 3
    if choices[155] == 1:
        sum += 2
    if choices[167] == 1:
        sum += 1
    if choices[168] == 1:
        sum += 3
    if choices[171] == 1:
        sum += 1
    if choices[173] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 43):
            sum = 43
        elif (sum > 48):
            sum = 48
    w[12] = sum
    r[12] = "Self-defeating"
    return sum


def eighta(person, choices, w, r):
    sum = 0
    if choices[1] == 1:
        sum += 1
    if choices[4] == 1:
        sum += 1
    if choices[9] == 1:
        sum += 2
    if choices[12] == 1:
        sum += 1
    if choices[16] == 1:
        sum += 2
    if choices[21] == 1:
        sum += 1
    if choices[22] == 1:
        sum += 3
    if choices[23] == 1:
        sum += 1
    if choices[25] == 1:
        sum += 1
    if choices[28] == 1:
        sum += 2
    if choices[43] == 1:
        sum += 2
    if choices[50] == 1:
        sum += 3
    if choices[51] == 1:
        sum += 1
    if choices[55] == 1:
        sum += 3
    if choices[58] == 1:
        sum += 1
    if choices[61] == 2:
        sum += 1
    if choices[64] == 1:
        sum += 2
    if choices[66] == 1:
        sum += 3
    if choices[73] == 1:
        sum += 2
    if choices[74] == 1:
        sum += 2
    if choices[77] == 1:
        sum += 2
    if choices[82] == 1:
        sum += 2
    if choices[86] == 1:
        sum += 2
    if choices[95] == 1:
        sum += 3
    if choices[101] == 1:
        sum += 2
    if choices[104] == 1:
        sum += 3
    if choices[107] == 1:
        sum += 3
    if choices[110] == 1:
        sum += 1
    if choices[115] == 1:
        sum += 2
    if choices[120] == 1:
        sum += 1
    if choices[123] == 1:
        sum += 2
    if choices[128] == 1:
        sum += 2
    if choices[129] == 1:
        sum += 1
    if choices[135] == 1:
        sum += 3
    if choices[139] == 1:
        sum += 1
    if choices[149] == 2:
        sum += 2
    if choices[155] == 1:
        sum += 2
    if choices[156] == 1:
        sum += 3
    if choices[159] == 2:
        sum += 2
    if choices[165] == 1:
        sum += 3
    if choices[171] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 55):
            sum = 55
        elif (sum > 53):
            sum = 53
    w[11] = sum
    r[11] = "Passive-Agressive"
    return sum


def seven(person, choices, w, r):
    sum = 0
    if choices[4] == 1:
        sum += 1
    if choices[7] == 2:
        sum += 1
    if choices[20] == 2:
        sum += 2
    if choices[21] == 1:
        sum += 3
    if choices[32] == 1:
        sum += 1
    if choices[39] == 1:
        sum += 3
    if choices[40] == 2:
        sum += 1
    if choices[43] == 2:
        sum += 1
    if choices[46] == 1:
        sum += 3
    if choices[48] == 2:
        sum += 2
    if choices[50] == 2:
        sum += 1
    if choices[60] == 2:
        sum += 1
    if choices[61] == 1:
        sum += 3
    if choices[64] == 1:
        sum += 2
    if choices[66] == 2:
        sum += 1
    if choices[74] == 1:
        sum += 1
    if choices[75] == 1:
        sum += 3
    if choices[77] == 2:
        sum += 1
    if choices[78] == 1:
        sum += 1
    if choices[81] == 1:
        sum += 1
    if choices[86] == 2:
        sum += 2
    if choices[88] == 1:
        sum += 3
    if choices[92] == 2:
        sum += 1
    if choices[95] == 2:
        sum += 1
    if choices[103] == 2:
        sum += 1
    if choices[111] == 2:
        sum += 1
    if choices[126] == 1:
        sum += 3
    if choices[128] == 2:
        sum += 1
    if choices[134] == 1:
        sum += 2
    if choices[138] == 1:
        sum += 3
    if choices[145] == 2:
        sum += 2
    if choices[148] == 1:
        sum += 2
    if choices[149] == 1:
        sum += 3
    if choices[153] == 1:
        sum += 3
    if choices[155] == 2:
        sum += 1
    if choices[159] == 1:
        sum += 2
    if choices[161] == 1:
        sum += 2
    if choices[163] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 61):
            sum = 61
        elif (sum > 60):
            sum = 60
    w[10] = sum
    r[10] = "Compulsive"
    return sum


def sixb(person, choices, w, r):
    sum = 0
    if choices[1] == 1:
        sum += 2
    if choices[4] == 1:
        sum += 3
    if choices[7] == 1:
        sum += 1
    if choices[9] == 1:
        sum += 3
    if choices[12] == 1:
        sum += 3
    if choices[21] == 1:
        sum += 2
    if choices[30] == 1:
        sum += 3
    if choices[31] == 2:
        sum += 1
    if choices[32] == 1:
        sum += 1
    if choices[38] == 1:
        sum += 1
    if choices[40] == 1:
        sum += 1
    if choices[41] == 1:
        sum += 3
    if choices[42] == 2:
        sum += 2
    if choices[43] == 1:
        sum += 1
    if choices[44] == 1:
        sum += 3
    if choices[58] == 1:
        sum += 1
    if choices[64] == 1:
        sum += 2
    if choices[66] == 1:
        sum += 1
    if choices[71] == 2:
        sum += 1
    if choices[74] == 1:
        sum += 2
    if choices[77] == 2:
        sum += 2
    if choices[78] == 2:
        sum += 2
    if choices[80] == 1:
        sum += 1
    if choices[82] == 1:
        sum += 2
    if choices[84] == 1:
        sum += 2
    if choices[86] == 1:
        sum += 1
    if choices[91] == 1:
        sum += 2
    if choices[95] == 1:
        sum += 1
    if choices[101] == 1:
        sum += 3
    if choices[106] == 2:
        sum += 1
    if choices[107] == 1:
        sum += 2
    if choices[115] == 1:
        sum += 2
    if choices[121] == 1:
        sum += 2
    if choices[129] == 1:
        sum += 2
    if choices[134] == 1:
        sum += 3
    if choices[135] == 1:
        sum += 1
    if choices[142] == 1:
        sum += 1
    if choices[145] == 2:
        sum += 1
    if choices[146] == 1:
        sum += 1
    if choices[147] == 1:
        sum += 1
    if choices[148] == 1:
        sum += 3
    if choices[155] == 1:
        sum += 2
    if choices[163] == 1:
        sum += 3
    if choices[165] == 1:
        sum += 1
    if choices[166] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 53):
            sum = 53
        elif (sum > 62):
            sum = 62
    w[9] = sum
    r[9] = "Aggressive/Sadistic"
    return sum


def sixa(person, choices, w, r):
    sum = 0
    if choices[1] == 1:
        sum += 2
    if choices[7] == 1:
        sum += 3
    if choices[12] == 1:
        sum += 2
    if choices[15] == 1:
        sum += 1
    if choices[20] == 1:
        sum += 2
    if choices[22] == 1:
        sum += 2
    if choices[32] == 1:
        sum += 2
    if choices[34] == 2:
        sum += 1
    if choices[38] == 1:
        sum += 2
    if choices[40] == 1:
        sum += 3
    if choices[42] == 2:
        sum += 2
    if choices[43] == 1:
        sum += 2
    if choices[44] == 1:
        sum += 1
    if choices[48] == 1:
        sum += 1
    if choices[55] == 1:
        sum += 2
    if choices[64] == 1:
        sum += 1
    if choices[73] == 1:
        sum += 2
    if choices[74] == 1:
        sum += 2
    if choices[77] == 2:
        sum += 1
    if choices[78] == 2:
        sum += 2
    if choices[80] == 1:
        sum += 2
    if choices[81] == 2:
        sum += 2
    if choices[85] == 1:
        sum += 1
    if choices[86] == 1:
        sum += 2
    if choices[87] == 1:
        sum += 2
    if choices[91] == 1:
        sum += 2
    if choices[92] == 1:
        sum += 3
    if choices[94] == 1:
        sum += 3
    if choices[101] == 1:
        sum += 1
    if choices[103] == 1:
        sum += 3
    if choices[104] == 1:
        sum += 1
    if choices[111] == 1:
        sum += 1
    if choices[113] == 1:
        sum += 1
    if choices[116] == 1:
        sum += 3
    if choices[129] == 1:
        sum += 2
    if choices[130] == 1:
        sum += 3
    if choices[140] == 1:
        sum += 1
    if choices[142] == 1:
        sum += 2
    if choices[144] == 1:
        sum += 2
    if choices[147] == 1:
        sum += 3
    if choices[157] == 1:
        sum += 1
    if choices[162] == 1:
        sum += 3
    if choices[165] == 1:
        sum += 2
    if choices[171] == 1:
        sum += 1
    if choices[172] == 1:
        sum += 3
    if person.sex == 0:
        if (sum > 54):
            sum = 54
        elif (sum > 56):
            sum = 56
    w[8] = sum
    r[8] = "Antisocial"
    return sum


def five(person, choices, w, r):
    sum = 0
    if choices[1] == 1:
        sum += 3
    if choices[2] == 1:
        sum += 1
    if choices[4] == 1:
        sum += 2
    if choices[6] == 1:
        sum += 3
    if choices[8] == 2:
        sum += 1
    if choices[12] == 1:
        sum += 1
    if choices[14] == 1:
        sum += 2
    if choices[15] == 1:
        sum += 3
    if choices[16] == 1:
        sum += 2
    if choices[22] == 1:
        sum += 1
    if choices[28] == 1:
        sum += 1
    if choices[31] == 2:
        sum += 1
    if choices[32] == 1:
        sum += 1
    if choices[37] == 1:
        sum += 3
    if choices[41] == 1:
        sum += 2
    if choices[42] == 2:
        sum += 2
    if choices[43] == 1:
        sum += 1
    if choices[45] == 2:
        sum += 1
    if choices[51] == 2:
        sum += 1
    if choices[55] == 1:
        sum += 1
    if choices[60] == 1:
        sum += 1
    if choices[78] == 2:
        sum += 1
    if choices[80] == 1:
        sum += 1
    if choices[85] == 1:
        sum += 1
    if choices[86] == 1:
        sum += 2
    if choices[89] == 1:
        sum += 3
    if choices[91] == 1:
        sum += 3
    if choices[103] == 1:
        sum += 2
    if choices[106] == 2:
        sum += 1
    if choices[111] == 1:
        sum += 2
    if choices[125] == 1:
        sum += 2
    if choices[126] == 1:
        sum += 1
    if choices[129] == 1:
        sum += 3
    if choices[130] == 1:
        sum += 1
    if choices[131] == 1:
        sum += 3
    if choices[134] == 1:
        sum += 1
    if choices[135] == 1:
        sum += 1
    if choices[137] == 1:
        sum += 2
    if choices[142] == 1:
        sum += 3
    if choices[143] == 1:
        sum += 1
    if choices[146] == 1:
        sum += 1
    if choices[149] == 2:
        sum += 2
    if choices[158] == 2:
        sum += 2
    if choices[163] == 1:
        sum += 1
    if choices[165] == 1:
        sum += 2
    if choices[166] == 1:
        sum += 3
    if choices[170] == 1:
        sum += 2
    if choices[171] == 1:
        sum += 2
    if choices[172] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 67):
            sum = 67
        elif (sum > 57):
            sum = 57
    w[7] = sum
    r[7] = "Narcissistic"
    return sum


def four(person, choices, w, r):
    sum = 0
    if choices[3] == 2:
        sum += 1
    if choices[7] == 1:
        sum += 1
    if choices[9] == 1:
        sum += 2
    if choices[14] == 1:
        sum += 3
    if choices[19] == 2:
        sum += 1
    if choices[20] == 1:
        sum += 3
    if choices[28] == 1:
        sum += 3
    if choices[37] == 1:
        sum += 1
    if choices[39] == 2:
        sum += 1
    if choices[40] == 1:
        sum += 1
    if choices[41] == 1:
        sum += 1
    if choices[42] == 1:
        sum += 2
    if choices[43] == 1:
        sum += 2
    if choices[48] == 1:
        sum += 3
    if choices[51] == 2:
        sum += 1
    if choices[56] == 1:
        sum += 1
    if choices[60] == 1:
        sum += 3
    if choices[61] == 2:
        sum += 2
    if choices[66] == 1:
        sum += 2
    if choices[77] == 2:
        sum += 1
    if choices[86] == 1:
        sum += 3
    if choices[89] == 1:
        sum += 1
    if choices[91] == 1:
        sum += 1
    if choices[95] == 1:
        sum += 1
    if choices[103] == 1:
        sum += 2
    if choices[111] == 1:
        sum += 3
    if choices[125] == 1:
        sum += 3
    if choices[126] == 2:
        sum += 1
    if choices[128] == 1:
        sum += 1
    if choices[130] == 1:
        sum += 1
    if choices[133] == 1:
        sum += 2
    if choices[137] == 1:
        sum += 3
    if choices[142] == 1:
        sum += 1
    if choices[158] == 2:
        sum += 2
    if choices[162] == 1:
        sum += 1
    if choices[166] == 1:
        sum += 2
    if choices[170] == 1:
        sum += 3
    if choices[171] == 1:
        sum += 1
    if choices[172] == 1:
        sum += 1
    if choices[173] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 58):
            sum = 58
        elif (sum > 52):
            sum = 52
    w[6] = sum
    r[6] = "Histrionic"
    return sum


def three(person, choices, w, r):
    sum = 0
    if choices[4] == 2:
        sum += 2
    if choices[7] == 2:
        sum += 1
    if choices[10] == 1:
        sum += 3
    if choices[12] == 2:
        sum += 1
    if choices[21] == 2:
        sum += 1
    if choices[28] == 2:
        sum += 1
    if choices[31] == 1:
        sum += 3
    if choices[34] == 1:
        sum += 2
    if choices[40] == 2:
        sum += 1
    if choices[41] == 2:
        sum += 1
    if choices[42] == 1:
        sum += 3
    if choices[43] == 2:
        sum += 1
    if choices[49] == 1:
        sum += 1
    if choices[54] == 1:
        sum += 1
    if choices[57] == 1:
        sum += 2
    if choices[60] == 1:
        sum += 2
    if choices[74] == 2:
        sum += 1
    if choices[75] == 1:
        sum += 1
    if choices[77] == 1:
        sum += 2
    if choices[78] == 1:
        sum += 3
    if choices[81] == 1:
        sum += 2
    if choices[91] == 2:
        sum += 1
    if choices[92] == 2:
        sum += 1
    if choices[97] == 1:
        sum += 2
    if choices[101] == 2:
        sum += 1
    if choices[106] == 1:
        sum += 3
    if choices[110] == 1:
        sum += 1
    if choices[125] == 1:
        sum += 1
    if choices[133] == 1:
        sum += 3
    if choices[145] == 1:
        sum += 3
    if choices[147] == 2:
        sum += 1
    if choices[149] == 1:
        sum += 1
    if choices[159] == 1:
        sum += 3
    if choices[162] == 2:
        sum += 1
    if choices[163] == 2:
        sum += 1
    if choices[168] == 1:
        sum += 1
    if choices[173] == 1:
        sum += 3
    if person.sex == 0:
        if (sum > 51):
            sum = 51
        elif (sum > 53):
            sum = 53
    w[5] = sum
    r[5] = "Dependent"
    return sum


def two(person, choices, w, r):
    sum = 0
    if choices[2] == 1:
        sum += 1
    if choices[3] == 1:
        sum += 3
    if choices[8] == 1:
        sum += 3
    if choices[14] == 2:
        sum += 1
    if choices[19] == 1:
        sum += 2
    if choices[21] == 2:
        sum += 1
    if choices[23] == 1:
        sum += 2
    if choices[25] == 1:
        sum += 2
    if choices[27] == 1:
        sum += 2
    if choices[28] == 2:
        sum += 1
    if choices[32] == 1:
        sum += 2
    if choices[34] == 1:
        sum += 1
    if choices[45] == 1:
        sum += 1
    if choices[47] == 1:
        sum += 2
    if choices[49] == 1:
        sum += 3
    if choices[56] == 1:
        sum += 2
    if choices[57] == 1:
        sum += 2
    if choices[63] == 1:
        sum += 3
    if choices[77] == 1:
        sum += 3
    if choices[81] == 1:
        sum += 1
    if choices[83] == 1:
        sum += 2
    if choices[85] == 1:
        sum += 1
    if choices[102] == 1:
        sum += 2
    if choices[106] == 1:
        sum += 1
    if choices[109] == 1:
        sum += 1
    if choices[110] == 1:
        sum += 2
    if choices[113] == 1:
        sum += 1
    if choices[115] == 1:
        sum += 2
    if choices[118] == 1:
        sum += 2
    if choices[120] == 1:
        sum += 3
    if choices[125] == 2:
        sum += 1
    if choices[133] == 1:
        sum += 1
    if choices[139] == 1:
        sum += 1
    if choices[141] == 1:
        sum += 3
    if choices[147] == 1:
        sum += 1
    if choices[150] == 1:
        sum += 2
    if choices[155] == 1:
        sum += 2
    if choices[158] == 1:
        sum += 3
    if choices[160] == 1:
        sum += 1
    if choices[163] == 2:
        sum += 1
    if choices[171] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 46):
            sum = 46
        elif (sum > 51):
            sum = 51
    w[4] = sum
    r[4] = "Avoidant"
    return sum


def one(person, choices, w, r):
    sum = 0
    if choices[2] == 1:
        sum += 3
    if choices[10] == 1:
        sum += 2
    if choices[13] == 1:
        sum += 3
    if choices[14] == 2:
        sum += 1
    if choices[16] == 1:
        sum += 1
    if choices[19] == 1:
        sum += 3
    if choices[20] == 2:
        sum += 2
    if choices[22] == 1:
        sum += 1
    if choices[25] == 1:
        sum += 1
    if choices[28] == 2:
        sum += 1
    if choices[33] == 1:
        sum += 2
    if choices[34] == 1:
        sum += 3
    if choices[46] == 1:
        sum += 1
    if choices[47] == 1:
        sum += 2
    if choices[48] == 2:
        sum += 2
    if choices[53] == 1:
        sum += 1
    if choices[60] == 2:
        sum += 1
    if choices[78] == 2:
        sum += 1
    if choices[81] == 1:
        sum += 3
    if choices[83] == 1:
        sum += 2
    if choices[85] == 1:
        sum += 1
    if choices[95] == 2:
        sum += 1
    if choices[103] == 2:
        sum += 1
    if choices[106] == 1:
        sum += 2
    if choices[108] == 1:
        sum += 1
    if choices[111] == 2:
        sum += 1
    if choices[124] == 1:
        sum += 2
    if choices[125] == 2:
        sum += 1
    if choices[159] == 1:
        sum += 1
    if choices[160] == 1:
        sum += 1
    if choices[161] == 1:
        sum += 3
    if choices[141] == 1:
        sum += 1
    if choices[142] == 1:
        sum += 1
    if choices[143] == 1:
        sum += 3
    if choices[150] == 1:
        sum += 2
    if person.sex == 0:
        if (sum > 40):
            sum = 40
        elif (sum > 44):
            sum = 44
    w[3] = sum
    r[3] = "Schizoid"
    return sum


def z(person, choices, w, r):
    sum = 0
    if choices[3] == 1:
        sum += 1
    if choices[5] == 1:
        sum += 1
    if choices[8] == 1:
        sum += 1
    if choices[18] == 1:
        sum += 1
    if choices[23] == 1:
        sum += 1
    if choices[24] == 1:
        sum += 1
    if choices[25] == 1:
        sum += 1
    if choices[26] == 1:
        sum += 1
    if choices[27] == 1:
        sum += 1
    if choices[33] == 1:
        sum += 1
    if choices[36] == 1:
        sum += 1
    if choices[43] == 1:
        sum += 1
    if choices[45] == 1:
        sum += 1
    if choices[49] == 1:
        sum += 1
    if choices[50] == 1:
        sum += 1
    if choices[51] == 1:
        sum += 1
    if choices[53] == 1:
        sum += 1
    if choices[54] == 1:
        sum += 1
    if choices[58] == 1:
        sum += 1
    if choices[59] == 1:
        sum += 1
    if choices[63] == 1:
        sum += 1
    if choices[66] == 1:
        sum += 1
    if choices[67] == 1:
        sum += 1
    if choices[68] == 1:
        sum += 1
    if choices[71] == 1:
        sum += 1
    if choices[72] == 1:
        sum += 1
    if choices[76] == 1:
        sum += 1
    if choices[79] == 1:
        sum += 1
    if choices[82] == 1:
        sum += 1
    if choices[96] == 1:
        sum += 1
    if choices[97] == 1:
        sum += 1
    if choices[99] == 1:
        sum += 1
    if choices[100] == 1:
        sum += 1
    if choices[102] == 1:
        sum += 1
    if choices[108] == 1:
        sum += 1
    if choices[110] == 1:
        sum += 1
    if choices[114] == 1:
        sum += 1
    if choices[115] == 1:
        sum += 1
    if choices[117] == 1:
        sum += 1
    if choices[118] == 1:
        sum += 1
    if choices[120] == 1:
        sum += 1
    if choices[128] == 1:
        sum += 1
    if choices[132] == 1:
        sum += 1
    if choices[136] == 1:
        sum += 1
    if choices[158] == 1:
        sum += 1
    if choices[167] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 34):
            sum = 34
        elif (sum > 35):
            sum = 35
    w[2] = sum
    r[2] = "Debasement"
    return sum


def y(person, choices, w, r):
    sum = 0
    if choices[4] == 1:
        sum += 1
    if choices[14] == 1:
        sum += 1
    if choices[34] == 1:
        sum += 1
    if choices[39] == 1:
        sum += 1
    if choices[60] == 1:
        sum += 1
    if choices[61] == 1:
        sum += 1
    if choices[75] == 1:
        sum += 1
    if choices[78] == 1:
        sum += 1
    if choices[86] == 1:
        sum += 1
    if choices[88] == 1:
        sum += 1
    if choices[89] == 1:
        sum += 1
    if choices[93] == 1:
        sum += 1
    if choices[103] == 1:
        sum += 1
    if choices[106] == 1:
        sum += 1
    if choices[122] == 1:
        sum += 1
    if choices[125] == 1:
        sum += 1
    if choices[126] == 1:
        sum += 1
    if choices[137] == 1:
        sum += 1
    if choices[138] == 1:
        sum += 1
    if choices[149] == 1:
        sum += 1
    if choices[153] == 1:
        sum += 1
    if choices[159] == 1:
        sum += 1
    if choices[166] == 1:
        sum += 1
    if person.sex == 0:
        if (sum > 22):
            sum = 22
        elif (sum > 21):
            sum = 21
    w[1] = sum
    r[1] = "Desirability"
    return sum


def checkonebr(onee):
    onebr = [0] * 41
    onebr[0] = 0
    onebr[1] = 0
    onebr[2] = 0
    onebr[3] = 0
    onebr[4] = 0
    onebr[5] = 0
    onebr[6] = 0
    onebr[7] = 13
    onebr[8] = 18
    onebr[9] = 23
    onebr[10] = 28
    onebr[11] = 33
    onebr[12] = 38
    onebr[13] = 43
    onebr[14] = 48
    onebr[15] = 53
    onebr[16] = 58
    onebr[17] = 63
    onebr[18] = 66
    onebr[19] = 67
    onebr[20] = 69
    onebr[21] = 70
    onebr[22] = 71
    onebr[23] = 71
    onebr[24] = 73
    onebr[25] = 74
    onebr[26] = 76
    onebr[27] = 78
    onebr[28] = 81
    onebr[29] = 83
    onebr[30] = 86
    onebr[31] = 88
    onebr[32] = 91
    onebr[33] = 96
    onebr[34] = 101
    onebr[35] = 106
    onebr[36] = 108
    onebr[37] = 109
    onebr[38] = 111
    onebr[39] = 116
    onebr[40] = 121
    return onebr[onee]


def checktwobr(twoe):
    twobr = [0] * 47
    twobr[0] = 6
    twobr[1] = 6
    twobr[2] = 6
    twobr[3] = 6
    twobr[4] = 6
    twobr[5] = 6
    twobr[6] = 6
    twobr[7] = 16
    twobr[8] = 26
    twobr[9] = 41
    twobr[10] = 44
    twobr[11] = 47
    twobr[12] = 50
    twobr[13] = 53
    twobr[14] = 57
    twobr[15] = 61
    twobr[16] = 66
    twobr[17] = 66
    twobr[18] = 67
    twobr[19] = 68
    twobr[20] = 68
    twobr[21] = 69
    twobr[22] = 71
    twobr[23] = 74
    twobr[24] = 76
    twobr[25] = 78
    twobr[26] = 81
    twobr[27] = 82
    twobr[28] = 83
    twobr[29] = 84
    twobr[30] = 86
    twobr[31] = 88
    twobr[32] = 90
    twobr[33] = 94
    twobr[34] = 97
    twobr[35] = 100
    twobr[36] = 101
    twobr[37] = 103
    twobr[38] = 105
    twobr[39] = 106
    twobr[40] = 108
    twobr[41] = 110
    twobr[42] = 112
    twobr[43] = 114
    twobr[44] = 116
    twobr[45] = 118
    twobr[46] = 121
    return twobr[twoe]


def checkthreebr(threee):
    threebr = [0] * 52
    threebr[0] = 0
    threebr[1] = 0
    threebr[2] = 0
    threebr[3] = 0
    threebr[4] = 0
    threebr[5] = 0
    threebr[6] = 0
    threebr[7] = 0
    threebr[8] = 0
    threebr[9] = 0
    threebr[10] = 0
    threebr[11] = 0
    threebr[12] = 0
    threebr[13] = 0
    threebr[14] = 0
    threebr[15] = 0
    threebr[16] = 0
    threebr[17] = 5
    threebr[18] = 10
    threebr[19] = 23
    threebr[20] = 34
    threebr[21] = 40
    threebr[22] = 42
    threebr[23] = 50
    threebr[24] = 59
    threebr[25] = 66
    threebr[26] = 66
    threebr[27] = 66
    threebr[28] = 69
    threebr[29] = 71
    threebr[30] = 72
    threebr[31] = 74
    threebr[32] = 77
    threebr[33] = 78
    threebr[34] = 80
    threebr[35] = 81
    threebr[36] = 85
    threebr[37] = 89
    threebr[38] = 91
    threebr[39] = 93
    threebr[40] = 94
    threebr[41] = 94
    threebr[42] = 94
    threebr[43] = 95
    threebr[44] = 96
    threebr[45] = 98
    threebr[46] = 100
    threebr[47] = 102
    threebr[48] = 106
    threebr[49] = 111
    threebr[50] = 116
    threebr[51] = 121
    return threebr[threee]


def checkfourbr(foure):
    fourbr = [0] * 59
    fourbr[0] = 6
    fourbr[1] = 6
    fourbr[2] = 6
    fourbr[3] = 6
    fourbr[4] = 6
    fourbr[5] = 6
    fourbr[6] = 6
    fourbr[7] = 6
    fourbr[8] = 6
    fourbr[9] = 6
    fourbr[10] = 6
    fourbr[11] = 6
    fourbr[12] = 6
    fourbr[13] = 6
    fourbr[14] = 11
    fourbr[15] = 13
    fourbr[16] = 16
    fourbr[17] = 18
    fourbr[18] = 26
    fourbr[19] = 36
    fourbr[20] = 41
    fourbr[21] = 44
    fourbr[22] = 47
    fourbr[23] = 50
    fourbr[24] = 53
    fourbr[25] = 55
    fourbr[26] = 57
    fourbr[27] = 59
    fourbr[28] = 61
    fourbr[29] = 63
    fourbr[30] = 66
    fourbr[31] = 67
    fourbr[32] = 68
    fourbr[33] = 69
    fourbr[34] = 70
    fourbr[35] = 71
    fourbr[36] = 73
    fourbr[37] = 74
    fourbr[38] = 76
    fourbr[39] = 78
    fourbr[40] = 79
    fourbr[41] = 80
    fourbr[42] = 81
    fourbr[43] = 82
    fourbr[44] = 83
    fourbr[45] = 85
    fourbr[46] = 87
    fourbr[47] = 89
    fourbr[48] = 90
    fourbr[49] = 91
    fourbr[50] = 94
    fourbr[51] = 96
    fourbr[52] = 99
    fourbr[53] = 103
    fourbr[54] = 108
    fourbr[55] = 112
    fourbr[56] = 116
    fourbr[57] = 118
    fourbr[58] = 121
    return fourbr[foure]


def checkfivebr(fivee):
    fivebr = [0] * 68
    fivebr[0] = 0
    fivebr[1] = 0
    fivebr[2] = 0
    fivebr[3] = 0
    fivebr[4] = 0
    fivebr[5] = 0
    fivebr[6] = 0
    fivebr[7] = 0
    fivebr[8] = 0
    fivebr[9] = 0
    fivebr[10] = 0
    fivebr[11] = 0
    fivebr[12] = 0
    fivebr[13] = 0
    fivebr[14] = 0
    fivebr[15] = 0
    fivebr[16] = 5
    fivebr[17] = 12
    fivebr[18] = 19
    fivebr[19] = 23
    fivebr[20] = 27
    fivebr[21] = 32
    fivebr[22] = 35
    fivebr[23] = 38
    fivebr[24] = 41
    fivebr[25] = 44
    fivebr[26] = 47
    fivebr[27] = 49
    fivebr[28] = 51
    fivebr[29] = 52
    fivebr[30] = 55
    fivebr[31] = 61
    fivebr[32] = 66
    fivebr[33] = 67
    fivebr[34] = 69
    fivebr[35] = 70
    fivebr[36] = 72
    fivebr[37] = 73
    fivebr[38] = 75
    fivebr[39] = 77
    fivebr[40] = 80
    fivebr[41] = 81
    fivebr[42] = 83
    fivebr[43] = 86
    fivebr[44] = 88
    fivebr[45] = 90
    fivebr[46] = 92
    fivebr[47] = 93
    fivebr[48] = 96
    fivebr[49] = 98
    fivebr[50] = 100
    fivebr[51] = 101
    fivebr[52] = 101
    fivebr[53] = 102
    fivebr[54] = 103
    fivebr[55] = 104
    fivebr[56] = 104
    fivebr[57] = 105
    fivebr[58] = 106
    fivebr[59] = 108
    fivebr[60] = 110
    fivebr[61] = 112
    fivebr[62] = 114
    fivebr[63] = 116
    fivebr[64] = 118
    fivebr[65] = 119
    fivebr[66] = 120
    fivebr[67] = 121
    return fivebr[fivee]


def checksixabr(sixae):
    sixabr = [0] * 55
    sixabr[0] = 0
    sixabr[1] = 0
    sixabr[2] = 0
    sixabr[3] = 0
    sixabr[4] = 0
    sixabr[5] = 0
    sixabr[6] = 0
    sixabr[7] = 0
    sixabr[8] = 9
    sixabr[9] = 13
    sixabr[10] = 17
    sixabr[11] = 22
    sixabr[12] = 27
    sixabr[13] = 32
    sixabr[14] = 37
    sixabr[15] = 42
    sixabr[16] = 44
    sixabr[17] = 47
    sixabr[18] = 49
    sixabr[19] = 52
    sixabr[20] = 54
    sixabr[21] = 57
    sixabr[22] = 59
    sixabr[23] = 62
    sixabr[24] = 64
    sixabr[25] = 66
    sixabr[26] = 67
    sixabr[27] = 68
    sixabr[28] = 69
    sixabr[29] = 70
    sixabr[30] = 71
    sixabr[31] = 72
    sixabr[32] = 73
    sixabr[33] = 74
    sixabr[34] = 75
    sixabr[35] = 77
    sixabr[36] = 79
    sixabr[37] = 81
    sixabr[38] = 83
    sixabr[39] = 85
    sixabr[40] = 87
    sixabr[41] = 88
    sixabr[42] = 91
    sixabr[43] = 94
    sixabr[44] = 98
    sixabr[45] = 101
    sixabr[46] = 104
    sixabr[47] = 106
    sixabr[48] = 108
    sixabr[49] = 110
    sixabr[50] = 112
    sixabr[51] = 114
    sixabr[52] = 116
    sixabr[53] = 118
    sixabr[54] = 121
    return sixabr[sixae]


def checksixbbr(sixbe):
    sixbbr = [0] * 54
    sixbbr[0] = 0
    sixbbr[1] = 0
    sixbbr[2] = 0
    sixbbr[3] = 0
    sixbbr[4] = 0
    sixbbr[5] = 0
    sixbbr[6] = 0
    sixbbr[7] = 0
    sixbbr[8] = 0
    sixbbr[9] = 0
    sixbbr[10] = 0
    sixbbr[11] = 0
    sixbbr[12] = 8
    sixbbr[13] = 15
    sixbbr[14] = 25
    sixbbr[15] = 35
    sixbbr[16] = 37
    sixbbr[17] = 39
    sixbbr[18] = 41
    sixbbr[19] = 43
    sixbbr[20] = 45
    sixbbr[21] = 47
    sixbbr[22] = 49
    sixbbr[23] = 50
    sixbbr[24] = 52
    sixbbr[25] = 54
    sixbbr[26] = 56
    sixbbr[27] = 62
    sixbbr[28] = 66
    sixbbr[29] = 67
    sixbbr[30] = 68
    sixbbr[31] = 70
    sixbbr[32] = 73
    sixbbr[33] = 75
    sixbbr[34] = 78
    sixbbr[35] = 79
    sixbbr[36] = 80
    sixbbr[37] = 83
    sixbbr[38] = 86
    sixbbr[39] = 88
    sixbbr[40] = 89
    sixbbr[41] = 93
    sixbbr[42] = 96
    sixbbr[43] = 98
    sixbbr[44] = 100
    sixbbr[45] = 102
    sixbbr[46] = 104
    sixbbr[47] = 105
    sixbbr[48] = 106
    sixbbr[49] = 114
    sixbbr[50] = 116
    sixbbr[51] = 118
    sixbbr[52] = 119
    sixbbr[53] = 121
    return sixbbr[sixbe]


def checksevenbr(sevene):
    sevenbr = [0] * 62
    sevenbr[0] = 6
    sevenbr[1] = 6
    sevenbr[2] = 6
    sevenbr[3] = 6
    sevenbr[4] = 6
    sevenbr[5] = 6
    sevenbr[6] = 6
    sevenbr[7] = 6
    sevenbr[8] = 6
    sevenbr[9] = 6
    sevenbr[10] = 6
    sevenbr[11] = 6
    sevenbr[12] = 6
    sevenbr[13] = 6
    sevenbr[14] = 6
    sevenbr[15] = 6
    sevenbr[16] = 6
    sevenbr[17] = 6
    sevenbr[18] = 11
    sevenbr[19] = 14
    sevenbr[20] = 18
    sevenbr[21] = 23
    sevenbr[22] = 26
    sevenbr[23] = 31
    sevenbr[24] = 34
    sevenbr[25] = 36
    sevenbr[26] = 39
    sevenbr[27] = 41
    sevenbr[28] = 46
    sevenbr[29] = 54
    sevenbr[30] = 59
    sevenbr[31] = 61
    sevenbr[32] = 61
    sevenbr[33] = 61
    sevenbr[34] = 61
    sevenbr[35] = 61
    sevenbr[36] = 62
    sevenbr[37] = 63
    sevenbr[38] = 64
    sevenbr[39] = 65
    sevenbr[40] = 67
    sevenbr[41] = 71
    sevenbr[42] = 75
    sevenbr[43] = 78
    sevenbr[44] = 80
    sevenbr[45] = 83
    sevenbr[46] = 86
    sevenbr[47] = 90
    sevenbr[48] = 93
    sevenbr[49] = 94
    sevenbr[50] = 95
    sevenbr[51] = 96
    sevenbr[52] = 97
    sevenbr[53] = 98
    sevenbr[54] = 102
    sevenbr[55] = 106
    sevenbr[56] = 108
    sevenbr[57] = 110
    sevenbr[58] = 113
    sevenbr[59] = 116
    sevenbr[60] = 118
    sevenbr[61] = 121
    return sevenbr[sevene]


def checkeightabr(eightae):
    eightabr = [0] * 56
    eightabr[0] = 0
    eightabr[1] = 0
    eightabr[2] = 0
    eightabr[3] = 0
    eightabr[4] = 0
    eightabr[5] = 0
    eightabr[6] = 0
    eightabr[7] = 2
    eightabr[8] = 7
    eightabr[9] = 12
    eightabr[10] = 17
    eightabr[11] = 22
    eightabr[12] = 27
    eightabr[13] = 32
    eightabr[14] = 34
    eightabr[15] = 36
    eightabr[16] = 38
    eightabr[17] = 40
    eightabr[18] = 42
    eightabr[19] = 44
    eightabr[20] = 47
    eightabr[21] = 49
    eightabr[22] = 51
    eightabr[23] = 55
    eightabr[24] = 62
    eightabr[25] = 66
    eightabr[26] = 67
    eightabr[27] = 68
    eightabr[28] = 69
    eightabr[29] = 70
    eightabr[30] = 71
    eightabr[31] = 74
    eightabr[32] = 76
    eightabr[33] = 78
    eightabr[34] = 81
    eightabr[35] = 85
    eightabr[36] = 88
    eightabr[37] = 90
    eightabr[38] = 94
    eightabr[39] = 98
    eightabr[40] = 102
    eightabr[41] = 105
    eightabr[42] = 107
    eightabr[43] = 108
    eightabr[44] = 110
    eightabr[45] = 111
    eightabr[46] = 111
    eightabr[47] = 112
    eightabr[48] = 113
    eightabr[49] = 114
    eightabr[50] = 116
    eightabr[51] = 117
    eightabr[52] = 118
    eightabr[53] = 119
    eightabr[54] = 120
    eightabr[55] = 121
    return eightabr[eightae]


def checkeightbbr(eightbe):
    eightbbr = [0] * 44
    eightbbr[0] = 0
    eightbbr[1] = 0
    eightbbr[2] = 0
    eightbbr[3] = 10
    eightbbr[4] = 20
    eightbbr[5] = 30
    eightbbr[6] = 35
    eightbbr[7] = 38
    eightbbr[8] = 41
    eightbbr[9] = 44
    eightbbr[10] = 47
    eightbbr[11] = 50
    eightbbr[12] = 55
    eightbbr[13] = 60
    eightbbr[14] = 61
    eightbbr[15] = 66
    eightbbr[16] = 67
    eightbbr[17] = 68
    eightbbr[18] = 69
    eightbbr[19] = 70
    eightbbr[20] = 71
    eightbbr[21] = 72
    eightbbr[22] = 73
    eightbbr[23] = 74
    eightbbr[24] = 74
    eightbbr[25] = 74
    eightbbr[26] = 75
    eightbbr[27] = 76
    eightbbr[28] = 76
    eightbbr[29] = 77
    eightbbr[30] = 78
    eightbbr[31] = 79
    eightbbr[32] = 81
    eightbbr[33] = 83
    eightbbr[34] = 89
    eightbbr[35] = 93
    eightbbr[36] = 98
    eightbbr[37] = 104
    eightbbr[38] = 111
    eightbbr[39] = 116
    eightbbr[40] = 119
    eightbbr[41] = 120
    eightbbr[42] = 120
    eightbbr[43] = 121
    return eightbbr[eightbe]


def checksbr(se):
    sbr = [0] * 49
    sbr[0] = 6
    sbr[1] = 6
    sbr[2] = 6
    sbr[3] = 16
    sbr[4] = 26
    sbr[5] = 36
    sbr[6] = 41
    sbr[7] = 43
    sbr[8] = 46
    sbr[9] = 48
    sbr[10] = 51
    sbr[11] = 53
    sbr[12] = 56
    sbr[13] = 58
    sbr[14] = 61
    sbr[15] = 63
    sbr[16] = 64
    sbr[17] = 64
    sbr[18] = 65
    sbr[19] = 65
    sbr[20] = 66
    sbr[21] = 66
    sbr[22] = 67
    sbr[23] = 67
    sbr[24] = 68
    sbr[25] = 68
    sbr[26] = 69
    sbr[27] = 69
    sbr[28] = 70
    sbr[29] = 70
    sbr[30] = 71
    sbr[31] = 71
    sbr[32] = 72
    sbr[33] = 72
    sbr[34] = 73
    sbr[35] = 73
    sbr[36] = 74
    sbr[37] = 75
    sbr[38] = 77
    sbr[39] = 81
    sbr[40] = 84
    sbr[41] = 87
    sbr[42] = 90
    sbr[43] = 97
    sbr[44] = 105
    sbr[45] = 110
    sbr[46] = 116
    sbr[47] = 119
    sbr[48] = 121
    return sbr[se]


def checkcbr(ce):
    cbr = [0] * 65
    cbr[0] = 0
    cbr[1] = 0
    cbr[2] = 0
    cbr[3] = 0
    cbr[4] = 0
    cbr[5] = 11
    cbr[6] = 16
    cbr[7] = 21
    cbr[8] = 26
    cbr[9] = 31
    cbr[10] = 36
    cbr[11] = 41
    cbr[12] = 42
    cbr[13] = 43
    cbr[14] = 44
    cbr[15] = 45
    cbr[16] = 46
    cbr[17] = 48
    cbr[18] = 50
    cbr[19] = 53
    cbr[20] = 56
    cbr[21] = 58
    cbr[22] = 59
    cbr[23] = 61
    cbr[24] = 63
    cbr[25] = 66
    cbr[26] = 66
    cbr[27] = 66
    cbr[28] = 66
    cbr[29] = 66
    cbr[30] = 66
    cbr[31] = 67
    cbr[32] = 68
    cbr[33] = 69
    cbr[34] = 70
    cbr[35] = 71
    cbr[36] = 72
    cbr[37] = 73
    cbr[38] = 73
    cbr[39] = 73
    cbr[40] = 74
    cbr[41] = 74
    cbr[42] = 75
    cbr[43] = 75
    cbr[44] = 75
    cbr[45] = 75
    cbr[46] = 76
    cbr[47] = 76
    cbr[48] = 77
    cbr[49] = 80
    cbr[50] = 84
    cbr[51] = 87
    cbr[52] = 92
    cbr[53] = 95
    cbr[54] = 97
    cbr[55] = 100
    cbr[56] = 104
    cbr[57] = 108
    cbr[58] = 110
    cbr[59] = 112
    cbr[60] = 114
    cbr[61] = 116
    cbr[62] = 118
    cbr[63] = 119
    cbr[64] = 121
    return cbr[ce]


def checkpbr(pe):
    pbr = [0] * 63
    pbr[0] = 0
    pbr[1] = 0
    pbr[2] = 0
    pbr[3] = 0
    pbr[4] = 0
    pbr[5] = 0
    pbr[6] = 12
    pbr[7] = 15
    pbr[8] = 17
    pbr[9] = 19
    pbr[10] = 27
    pbr[11] = 37
    pbr[12] = 42
    pbr[13] = 45
    pbr[14] = 49
    pbr[15] = 52
    pbr[16] = 53
    pbr[17] = 54
    pbr[18] = 55
    pbr[19] = 56
    pbr[20] = 57
    pbr[21] = 58
    pbr[22] = 59
    pbr[23] = 60
    pbr[24] = 61
    pbr[25] = 62
    pbr[26] = 63
    pbr[27] = 64
    pbr[28] = 65
    pbr[29] = 65
    pbr[30] = 66
    pbr[31] = 66
    pbr[32] = 67
    pbr[33] = 68
    pbr[34] = 69
    pbr[35] = 69
    pbr[36] = 70
    pbr[37] = 70
    pbr[38] = 71
    pbr[39] = 72
    pbr[40] = 72
    pbr[41] = 73
    pbr[42] = 73
    pbr[43] = 74
    pbr[44] = 75
    pbr[45] = 77
    pbr[46] = 80
    pbr[47] = 82
    pbr[48] = 85
    pbr[49] = 88
    pbr[50] = 92
    pbr[51] = 95
    pbr[52] = 98
    pbr[53] = 100
    pbr[54] = 102
    pbr[55] = 104
    pbr[56] = 107
    pbr[57] = 109
    pbr[58] = 111
    pbr[59] = 113
    pbr[60] = 117
    pbr[61] = 120
    pbr[62] = 121
    return pbr[pe]


def checkabr(ae):
    abr = [0] * 37
    abr[0] = 0
    abr[1] = 0
    abr[2] = 0
    abr[3] = 20
    abr[4] = 30
    abr[5] = 40
    abr[6] = 50
    abr[7] = 60
    abr[8] = 62
    abr[9] = 64
    abr[10] = 66
    abr[11] = 70
    abr[12] = 72
    abr[13] = 75
    abr[14] = 77
    abr[15] = 79
    abr[16] = 81
    abr[17] = 83
    abr[18] = 85
    abr[19] = 86
    abr[20] = 87
    abr[21] = 88
    abr[22] = 89
    abr[23] = 90
    abr[24] = 90
    abr[25] = 90
    abr[26] = 91
    abr[27] = 93
    abr[28] = 95
    abr[29] = 96
    abr[30] = 98
    abr[31] = 100
    abr[32] = 102
    abr[33] = 105
    abr[34] = 109
    abr[35] = 113
    abr[36] = 115
    return abr[ae]


def checkhbr(he):
    hbr = [0] * 44
    hbr[0] = 0
    hbr[1] = 0
    hbr[2] = 0
    hbr[3] = 15
    hbr[4] = 30
    hbr[5] = 40
    hbr[6] = 48
    hbr[7] = 55
    hbr[8] = 57
    hbr[9] = 58
    hbr[10] = 59
    hbr[11] = 59
    hbr[12] = 60
    hbr[13] = 60
    hbr[14] = 61
    hbr[15] = 61
    hbr[16] = 62
    hbr[17] = 62
    hbr[18] = 63
    hbr[19] = 63
    hbr[20] = 64
    hbr[21] = 64
    hbr[22] = 65
    hbr[23] = 65
    hbr[24] = 66
    hbr[25] = 66
    hbr[26] = 67
    hbr[27] = 67
    hbr[28] = 67
    hbr[29] = 68
    hbr[30] = 68
    hbr[31] = 68
    hbr[32] = 69
    hbr[33] = 70
    hbr[34] = 72
    hbr[35] = 75
    hbr[36] = 83
    hbr[37] = 87
    hbr[38] = 92
    hbr[39] = 96
    hbr[40] = 100
    hbr[41] = 105
    hbr[42] = 110
    hbr[43] = 115
    return hbr[he]


def checknbr(ne):
    nbr = [0] * 45
    nbr[0] = 0
    nbr[1] = 0
    nbr[2] = 0
    nbr[3] = 0
    nbr[4] = 0
    nbr[5] = 0
    nbr[6] = 2
    nbr[7] = 5
    nbr[8] = 10
    nbr[9] = 12
    nbr[10] = 20
    nbr[11] = 30
    nbr[12] = 35
    nbr[13] = 37
    nbr[14] = 39
    nbr[15] = 41
    nbr[16] = 44
    nbr[17] = 47
    nbr[18] = 50
    nbr[19] = 53
    nbr[20] = 57
    nbr[21] = 60
    nbr[22] = 60
    nbr[23] = 60
    nbr[24] = 60
    nbr[25] = 60
    nbr[26] = 60
    nbr[27] = 60
    nbr[28] = 61
    nbr[29] = 62
    nbr[30] = 63
    nbr[31] = 64
    nbr[32] = 65
    nbr[33] = 67
    nbr[34] = 69
    nbr[35] = 71
    nbr[36] = 73
    nbr[37] = 75
    nbr[38] = 79
    nbr[39] = 82
    nbr[40] = 85
    nbr[41] = 90
    nbr[42] = 95
    nbr[43] = 110
    nbr[44] = 115
    return nbr[ne]


def checkdbr(de):
    dbr = [0] * 57
    dbr[0] = 0
    dbr[1] = 0
    dbr[2] = 0
    dbr[3] = 0
    dbr[4] = 10
    dbr[5] = 15
    dbr[6] = 18
    dbr[7] = 21
    dbr[8] = 25
    dbr[9] = 27
    dbr[10] = 30
    dbr[11] = 32
    dbr[12] = 35
    dbr[13] = 42
    dbr[14] = 49
    dbr[15] = 55
    dbr[16] = 58
    dbr[17] = 59
    dbr[18] = 61
    dbr[19] = 63
    dbr[20] = 71
    dbr[21] = 73
    dbr[22] = 74
    dbr[23] = 76
    dbr[24] = 80
    dbr[25] = 85
    dbr[26] = 87
    dbr[27] = 88
    dbr[28] = 89
    dbr[29] = 90
    dbr[30] = 90
    dbr[31] = 90
    dbr[32] = 91
    dbr[33] = 91
    dbr[34] = 92
    dbr[35] = 92
    dbr[36] = 93
    dbr[37] = 93
    dbr[38] = 93
    dbr[39] = 94
    dbr[40] = 94
    dbr[41] = 95
    dbr[42] = 96
    dbr[43] = 96
    dbr[44] = 97
    dbr[45] = 98
    dbr[46] = 98
    dbr[47] = 99
    dbr[48] = 99
    dbr[49] = 100
    dbr[50] = 100
    dbr[51] = 104
    dbr[52] = 107
    dbr[53] = 110
    dbr[54] = 112
    dbr[55] = 114
    dbr[56] = 115
    return dbr[de]


def checkbbr(be):
    bbr = [0] * 52
    bbr[0] = 0
    bbr[1] = 0
    bbr[2] = 0
    bbr[3] = 0
    bbr[4] = 0
    bbr[5] = 0
    bbr[6] = 0
    bbr[7] = 0
    bbr[8] = 15
    bbr[9] = 25
    bbr[10] = 35
    bbr[11] = 38
    bbr[12] = 41
    bbr[13] = 45
    bbr[14] = 48
    bbr[15] = 51
    bbr[16] = 55
    bbr[17] = 60
    bbr[18] = 61
    bbr[19] = 62
    bbr[20] = 63
    bbr[21] = 64
    bbr[22] = 65
    bbr[23] = 67
    bbr[24] = 69
    bbr[25] = 71
    bbr[26] = 73
    bbr[27] = 75
    bbr[28] = 77
    bbr[29] = 79
    bbr[30] = 81
    bbr[31] = 83
    bbr[32] = 85
    bbr[33] = 86
    bbr[34] = 88
    bbr[35] = 89
    bbr[36] = 90
    bbr[37] = 92
    bbr[38] = 93
    bbr[39] = 94
    bbr[40] = 95
    bbr[41] = 97
    bbr[42] = 98
    bbr[43] = 99
    bbr[44] = 100
    bbr[45] = 101
    bbr[46] = 103
    bbr[47] = 105
    bbr[48] = 108
    bbr[49] = 111
    bbr[50] = 113
    bbr[51] = 115
    return bbr[be]


def checktbr(te):
    tbr = [0] * 61
    tbr[0] = 0
    tbr[1] = 0
    tbr[2] = 0
    tbr[3] = 0
    tbr[4] = 0
    tbr[5] = 0
    tbr[6] = 0
    tbr[7] = 5
    tbr[8] = 10
    tbr[9] = 15
    tbr[10] = 20
    tbr[11] = 25
    tbr[12] = 30
    tbr[13] = 35
    tbr[14] = 37
    tbr[15] = 39
    tbr[16] = 41
    tbr[17] = 44
    tbr[18] = 48
    tbr[19] = 51
    tbr[20] = 54
    tbr[21] = 57
    tbr[22] = 60
    tbr[23] = 60
    tbr[24] = 60
    tbr[25] = 61
    tbr[26] = 61
    tbr[27] = 62
    tbr[28] = 63
    tbr[29] = 64
    tbr[30] = 65
    tbr[31] = 66
    tbr[32] = 68
    tbr[33] = 69
    tbr[34] = 70
    tbr[35] = 71
    tbr[36] = 72
    tbr[37] = 73
    tbr[38] = 75
    tbr[39] = 77
    tbr[40] = 79
    tbr[41] = 81
    tbr[42] = 83
    tbr[43] = 85
    tbr[44] = 86
    tbr[45] = 87
    tbr[46] = 89
    tbr[47] = 90
    tbr[48] = 91
    tbr[49] = 92
    tbr[50] = 94
    tbr[51] = 95
    tbr[52] = 97
    tbr[53] = 98
    tbr[54] = 99
    tbr[55] = 100
    tbr[56] = 103
    tbr[57] = 106
    tbr[58] = 109
    tbr[59] = 112
    tbr[60] = 115
    return tbr[te]


def checkssbr(sse):
    ssbr = [0] * 40
    ssbr[0] = 0
    ssbr[1] = 0
    ssbr[2] = 0
    ssbr[3] = 35
    ssbr[4] = 40
    ssbr[5] = 44
    ssbr[6] = 50
    ssbr[7] = 55
    ssbr[8] = 60
    ssbr[9] = 60
    ssbr[10] = 60
    ssbr[11] = 60
    ssbr[12] = 60
    ssbr[13] = 61
    ssbr[14] = 61
    ssbr[15] = 62
    ssbr[16] = 62
    ssbr[17] = 63
    ssbr[18] = 65
    ssbr[19] = 67
    ssbr[20] = 67
    ssbr[21] = 68
    ssbr[22] = 68
    ssbr[23] = 69
    ssbr[24] = 70
    ssbr[25] = 70
    ssbr[26] = 71
    ssbr[27] = 72
    ssbr[28] = 73
    ssbr[29] = 75
    ssbr[30] = 77
    ssbr[31] = 79
    ssbr[32] = 80
    ssbr[33] = 82
    ssbr[34] = 85
    ssbr[35] = 90
    ssbr[36] = 95
    ssbr[37] = 100
    ssbr[38] = 110
    ssbr[39] = 115
    return ssbr[sse]


def checkccbr(cce):
    ccbr = [0] * 47
    ccbr[0] = 0
    ccbr[1] = 35
    ccbr[2] = 38
    ccbr[3] = 41
    ccbr[4] = 44
    ccbr[5] = 47
    ccbr[6] = 50
    ccbr[7] = 55
    ccbr[8] = 60
    ccbr[9] = 60
    ccbr[10] = 60
    ccbr[11] = 60
    ccbr[12] = 60
    ccbr[13] = 60
    ccbr[14] = 60
    ccbr[15] = 60
    ccbr[16] = 60
    ccbr[17] = 60
    ccbr[18] = 61
    ccbr[19] = 62
    ccbr[20] = 63
    ccbr[21] = 64
    ccbr[22] = 65
    ccbr[23] = 65
    ccbr[24] = 66
    ccbr[25] = 67
    ccbr[26] = 68
    ccbr[27] = 69
    ccbr[28] = 70
    ccbr[29] = 71
    ccbr[30] = 72
    ccbr[31] = 73
    ccbr[32] = 74
    ccbr[33] = 75
    ccbr[34] = 75
    ccbr[35] = 76
    ccbr[36] = 77
    ccbr[37] = 78
    ccbr[38] = 79
    ccbr[39] = 80
    ccbr[40] = 83
    ccbr[41] = 85
    ccbr[42] = 90
    ccbr[43] = 95
    ccbr[44] = 100
    ccbr[45] = 110
    ccbr[46] = 115
    return ccbr[cce]


def checkppbr(ppe):
    ppbr = [0] * 37
    ppbr[0] = 0
    ppbr[1] = 0
    ppbr[2] = 0
    ppbr[3] = 10
    ppbr[4] = 25
    ppbr[5] = 35
    ppbr[6] = 38
    ppbr[7] = 41
    ppbr[8] = 44
    ppbr[9] = 47
    ppbr[10] = 51
    ppbr[11] = 53
    ppbr[12] = 55
    ppbr[13] = 57
    ppbr[14] = 60
    ppbr[15] = 60
    ppbr[16] = 60
    ppbr[17] = 61
    ppbr[18] = 63
    ppbr[19] = 64
    ppbr[20] = 65
    ppbr[21] = 67
    ppbr[22] = 69
    ppbr[23] = 71
    ppbr[24] = 72
    ppbr[25] = 73
    ppbr[26] = 75
    ppbr[27] = 80
    ppbr[28] = 85
    ppbr[29] = 88
    ppbr[30] = 91
    ppbr[31] = 94
    ppbr[32] = 97
    ppbr[33] = 100
    ppbr[34] = 105
    ppbr[35] = 110
    ppbr[36] = 115
    return ppbr[ppe]


def checkybr(ye):
    ybr = [0] * 23
    ybr[0] = 0
    ybr[1] = 5
    ybr[2] = 10
    ybr[3] = 15
    ybr[4] = 20
    ybr[5] = 25
    ybr[6] = 30
    ybr[7] = 34
    ybr[8] = 39
    ybr[9] = 43
    ybr[10] = 46
    ybr[11] = 50
    ybr[12] = 56
    ybr[13] = 62
    ybr[14] = 67
    ybr[15] = 72
    ybr[16] = 75
    ybr[17] = 78
    ybr[18] = 82
    ybr[19] = 85
    ybr[20] = 90
    ybr[21] = 95
    ybr[22] = 100
    return ybr[ye]


def checkzbr(ze):
    zbr = [0] * 35
    zbr[0] = 12
    zbr[1] = 24
    zbr[2] = 35
    zbr[3] = 38
    zbr[4] = 42
    zbr[5] = 45
    zbr[6] = 48
    zbr[7] = 52
    zbr[8] = 55
    zbr[9] = 57
    zbr[10] = 59
    zbr[11] = 61
    zbr[12] = 63
    zbr[13] = 65
    zbr[14] = 67
    zbr[15] = 69
    zbr[16] = 70
    zbr[17] = 71
    zbr[18] = 73
    zbr[19] = 75
    zbr[20] = 76
    zbr[21] = 77
    zbr[22] = 78
    zbr[23] = 79
    zbr[24] = 80
    zbr[25] = 82
    zbr[26] = 84
    zbr[27] = 85
    zbr[28] = 87
    zbr[29] = 89
    zbr[30] = 91
    zbr[31] = 93
    zbr[32] = 95
    zbr[33] = 97
    zbr[34] = 100
    return zbr[ze]


def checkfonebr(fonee):
    fonebr = [0] * 45
    fonebr[0] = 0
    fonebr[1] = 0
    fonebr[2] = 0
    fonebr[3] = 0
    fonebr[4] = 0
    fonebr[5] = 0
    fonebr[6] = 0
    fonebr[7] = 0
    fonebr[8] = 0
    fonebr[9] = 0
    fonebr[10] = 15
    fonebr[11] = 35
    fonebr[12] = 47
    fonebr[13] = 50
    fonebr[14] = 53
    fonebr[15] = 56
    fonebr[16] = 60
    fonebr[17] = 62
    fonebr[18] = 64
    fonebr[19] = 65
    fonebr[20] = 66
    fonebr[21] = 67
    fonebr[22] = 68
    fonebr[23] = 69
    fonebr[24] = 70
    fonebr[25] = 71
    fonebr[26] = 72
    fonebr[27] = 73
    fonebr[28] = 74
    fonebr[29] = 75
    fonebr[30] = 76
    fonebr[31] = 77
    fonebr[32] = 78
    fonebr[33] = 79
    fonebr[34] = 81
    fonebr[35] = 84
    fonebr[36] = 86
    fonebr[37] = 88
    fonebr[38] = 90
    fonebr[39] = 91
    fonebr[40] = 96
    fonebr[41] = 104
    fonebr[42] = 111
    fonebr[43] = 118
    fonebr[44] = 121
    return fonebr[fonee]


def checkftwobr(ftwoe):
    ftwobr = [0] * 52
    ftwobr[0] = 0
    ftwobr[1] = 0
    ftwobr[2] = 0
    ftwobr[3] = 0
    ftwobr[4] = 0
    ftwobr[5] = 15
    ftwobr[6] = 21
    ftwobr[7] = 31
    ftwobr[8] = 41
    ftwobr[9] = 44
    ftwobr[10] = 48
    ftwobr[11] = 51
    ftwobr[12] = 53
    ftwobr[13] = 60
    ftwobr[14] = 64
    ftwobr[15] = 66
    ftwobr[16] = 67
    ftwobr[17] = 69
    ftwobr[18] = 70
    ftwobr[19] = 71
    ftwobr[20] = 72
    ftwobr[21] = 73
    ftwobr[22] = 74
    ftwobr[23] = 75
    ftwobr[24] = 76
    ftwobr[25] = 76
    ftwobr[26] = 77
    ftwobr[27] = 78
    ftwobr[28] = 79
    ftwobr[29] = 80
    ftwobr[30] = 81
    ftwobr[31] = 83
    ftwobr[32] = 85
    ftwobr[33] = 87
    ftwobr[34] = 88
    ftwobr[35] = 89
    ftwobr[36] = 90
    ftwobr[37] = 91
    ftwobr[38] = 94
    ftwobr[39] = 97
    ftwobr[40] = 100
    ftwobr[41] = 102
    ftwobr[42] = 104
    ftwobr[43] = 105
    ftwobr[44] = 106
    ftwobr[45] = 108
    ftwobr[46] = 110
    ftwobr[47] = 111
    ftwobr[48] = 116
    ftwobr[49] = 118
    ftwobr[50] = 120
    ftwobr[51] = 121
    return ftwobr[ftwoe]


def checkfthreebr(fthreee):
    fthreebr = [0] * 54
    fthreebr[0] = 0
    fthreebr[1] = 0
    fthreebr[2] = 0
    fthreebr[3] = 0
    fthreebr[4] = 0
    fthreebr[5] = 0
    fthreebr[6] = 0
    fthreebr[7] = 0
    fthreebr[8] = 0
    fthreebr[9] = 0
    fthreebr[10] = 0
    fthreebr[11] = 0
    fthreebr[12] = 0
    fthreebr[13] = 0
    fthreebr[14] = 0
    fthreebr[15] = 0
    fthreebr[16] = 0
    fthreebr[17] = 0
    fthreebr[18] = 5
    fthreebr[19] = 10
    fthreebr[20] = 15
    fthreebr[21] = 20
    fthreebr[22] = 30
    fthreebr[23] = 37
    fthreebr[24] = 45
    fthreebr[25] = 55
    fthreebr[26] = 66
    fthreebr[27] = 68
    fthreebr[28] = 69
    fthreebr[29] = 70
    fthreebr[30] = 71
    fthreebr[31] = 72
    fthreebr[32] = 75
    fthreebr[33] = 78
    fthreebr[34] = 81
    fthreebr[35] = 84
    fthreebr[36] = 87
    fthreebr[37] = 89
    fthreebr[38] = 91
    fthreebr[39] = 93
    fthreebr[40] = 95
    fthreebr[41] = 97
    fthreebr[42] = 99
    fthreebr[43] = 101
    fthreebr[44] = 102
    fthreebr[45] = 103
    fthreebr[46] = 103
    fthreebr[47] = 104
    fthreebr[48] = 105
    fthreebr[49] = 108
    fthreebr[50] = 112
    fthreebr[51] = 116
    fthreebr[52] = 118
    fthreebr[53] = 121
    return fthreebr[fthreee]


def checkffourbr(ffoure):
    ffourbr = [0] * 53
    ffourbr[0] = 0
    ffourbr[1] = 0
    ffourbr[2] = 0
    ffourbr[3] = 0
    ffourbr[4] = 0
    ffourbr[5] = 0
    ffourbr[6] = 0
    ffourbr[7] = 0
    ffourbr[8] = 0
    ffourbr[9] = 0
    ffourbr[10] = 0
    ffourbr[11] = 11
    ffourbr[12] = 15
    ffourbr[13] = 18
    ffourbr[14] = 21
    ffourbr[15] = 24
    ffourbr[16] = 31
    ffourbr[17] = 36
    ffourbr[18] = 41
    ffourbr[19] = 49
    ffourbr[20] = 56
    ffourbr[21] = 58
    ffourbr[22] = 59
    ffourbr[23] = 61
    ffourbr[24] = 62
    ffourbr[25] = 63
    ffourbr[26] = 64
    ffourbr[27] = 66
    ffourbr[28] = 69
    ffourbr[29] = 70
    ffourbr[30] = 74
    ffourbr[31] = 78
    ffourbr[32] = 79
    ffourbr[33] = 80
    ffourbr[34] = 81
    ffourbr[35] = 81
    ffourbr[36] = 82
    ffourbr[37] = 83
    ffourbr[38] = 84
    ffourbr[39] = 86
    ffourbr[40] = 89
    ffourbr[41] = 91
    ffourbr[42] = 92
    ffourbr[43] = 93
    ffourbr[44] = 93
    ffourbr[45] = 94
    ffourbr[46] = 94
    ffourbr[47] = 96
    ffourbr[48] = 97
    ffourbr[49] = 99
    ffourbr[50] = 101
    ffourbr[51] = 106
    ffourbr[52] = 121
    return ffourbr[ffoure]


def checkffivebr(ffivee):
    ffivebr = [0] * 58
    ffivebr[0] = 0
    ffivebr[1] = 0
    ffivebr[2] = 0
    ffivebr[3] = 0
    ffivebr[4] = 0
    ffivebr[5] = 0
    ffivebr[6] = 0
    ffivebr[7] = 0
    ffivebr[8] = 0
    ffivebr[9] = 0
    ffivebr[10] = 0
    ffivebr[11] = 0
    ffivebr[12] = 0
    ffivebr[13] = 0
    ffivebr[14] = 0
    ffivebr[15] = 0
    ffivebr[16] = 3
    ffivebr[17] = 6
    ffivebr[18] = 13
    ffivebr[19] = 23
    ffivebr[20] = 33
    ffivebr[21] = 35
    ffivebr[22] = 38
    ffivebr[23] = 40
    ffivebr[24] = 43
    ffivebr[25] = 45
    ffivebr[26] = 48
    ffivebr[27] = 52
    ffivebr[28] = 58
    ffivebr[29] = 66
    ffivebr[30] = 67
    ffivebr[31] = 68
    ffivebr[32] = 69
    ffivebr[33] = 70
    ffivebr[34] = 71
    ffivebr[35] = 72
    ffivebr[36] = 73
    ffivebr[37] = 74
    ffivebr[38] = 75
    ffivebr[39] = 76
    ffivebr[40] = 77
    ffivebr[41] = 78
    ffivebr[42] = 79
    ffivebr[43] = 80
    ffivebr[44] = 81
    ffivebr[45] = 82
    ffivebr[46] = 84
    ffivebr[47] = 85
    ffivebr[48] = 86
    ffivebr[49] = 87
    ffivebr[50] = 89
    ffivebr[51] = 91
    ffivebr[52] = 96
    ffivebr[53] = 101
    ffivebr[54] = 106
    ffivebr[55] = 112
    ffivebr[56] = 118
    ffivebr[57] = 121
    return ffivebr[ffivee]


def checkfsixabr(fsixae):
    fsixabr = [0] * 57
    fsixabr[0] = 0
    fsixabr[1] = 0
    fsixabr[2] = 0
    fsixabr[3] = 0
    fsixabr[4] = 0
    fsixabr[5] = 0
    fsixabr[6] = 0
    fsixabr[7] = 0
    fsixabr[8] = 0
    fsixabr[9] = 12
    fsixabr[10] = 17
    fsixabr[11] = 22
    fsixabr[12] = 27
    fsixabr[13] = 32
    fsixabr[14] = 42
    fsixabr[15] = 45
    fsixabr[16] = 47
    fsixabr[17] = 50
    fsixabr[18] = 52
    fsixabr[19] = 57
    fsixabr[20] = 58
    fsixabr[21] = 59
    fsixabr[22] = 61
    fsixabr[23] = 62
    fsixabr[24] = 63
    fsixabr[25] = 64
    fsixabr[26] = 65
    fsixabr[27] = 66
    fsixabr[28] = 66
    fsixabr[29] = 66
    fsixabr[30] = 67
    fsixabr[31] = 69
    fsixabr[32] = 70
    fsixabr[33] = 72
    fsixabr[34] = 73
    fsixabr[35] = 75
    fsixabr[36] = 76
    fsixabr[37] = 78
    fsixabr[38] = 79
    fsixabr[39] = 80
    fsixabr[40] = 81
    fsixabr[41] = 85
    fsixabr[42] = 87
    fsixabr[43] = 89
    fsixabr[44] = 90
    fsixabr[45] = 90
    fsixabr[46] = 91
    fsixabr[47] = 95
    fsixabr[48] = 98
    fsixabr[49] = 100
    fsixabr[50] = 102
    fsixabr[51] = 103
    fsixabr[52] = 105
    fsixabr[53] = 106
    fsixabr[54] = 111
    fsixabr[55] = 116
    fsixabr[56] = 121
    return fsixabr[fsixae]


def checkfsixbbr(fsixbe):
    fsixbbr = [0] * 63
    fsixbbr[0] = 0
    fsixbbr[1] = 0
    fsixbbr[2] = 0
    fsixbbr[3] = 0
    fsixbbr[4] = 0
    fsixbbr[5] = 0
    fsixbbr[6] = 0
    fsixbbr[7] = 0
    fsixbbr[8] = 0
    fsixbbr[9] = 0
    fsixbbr[10] = 5
    fsixbbr[11] = 10
    fsixbbr[12] = 12
    fsixbbr[13] = 16
    fsixbbr[14] = 20
    fsixbbr[15] = 24
    fsixbbr[16] = 30
    fsixbbr[17] = 35
    fsixbbr[18] = 37
    fsixbbr[19] = 39
    fsixbbr[20] = 42
    fsixbbr[21] = 44
    fsixbbr[22] = 49
    fsixbbr[23] = 55
    fsixbbr[24] = 60
    fsixbbr[25] = 66
    fsixbbr[26] = 67
    fsixbbr[27] = 68
    fsixbbr[28] = 69
    fsixbbr[29] = 70
    fsixbbr[30] = 71
    fsixbbr[31] = 72
    fsixbbr[32] = 73
    fsixbbr[33] = 74
    fsixbbr[34] = 75
    fsixbbr[35] = 76
    fsixbbr[36] = 76
    fsixbbr[37] = 77
    fsixbbr[38] = 78
    fsixbbr[39] = 79
    fsixbbr[40] = 80
    fsixbbr[41] = 81
    fsixbbr[42] = 83
    fsixbbr[43] = 84
    fsixbbr[44] = 85
    fsixbbr[45] = 86
    fsixbbr[46] = 87
    fsixbbr[47] = 88
    fsixbbr[48] = 89
    fsixbbr[49] = 90
    fsixbbr[50] = 91
    fsixbbr[51] = 93
    fsixbbr[52] = 95
    fsixbbr[53] = 97
    fsixbbr[54] = 99
    fsixbbr[55] = 101
    fsixbbr[56] = 103
    fsixbbr[57] = 106
    fsixbbr[58] = 111
    fsixbbr[59] = 115
    fsixbbr[60] = 117
    fsixbbr[61] = 119
    fsixbbr[62] = 121
    return fsixbbr[fsixbe]


def checkfsevenbr(fsevene):
    fsevenbr = [0] * 61
    fsevenbr[0] = 0
    fsevenbr[1] = 0
    fsevenbr[2] = 0
    fsevenbr[3] = 0
    fsevenbr[4] = 0
    fsevenbr[5] = 0
    fsevenbr[6] = 0
    fsevenbr[7] = 0
    fsevenbr[8] = 0
    fsevenbr[9] = 0
    fsevenbr[10] = 0
    fsevenbr[11] = 0
    fsevenbr[12] = 0
    fsevenbr[13] = 0
    fsevenbr[14] = 0
    fsevenbr[15] = 0
    fsevenbr[16] = 0
    fsevenbr[17] = 0
    fsevenbr[18] = 0
    fsevenbr[19] = 0
    fsevenbr[20] = 10
    fsevenbr[21] = 14
    fsevenbr[22] = 16
    fsevenbr[23] = 21
    fsevenbr[24] = 26
    fsevenbr[25] = 31
    fsevenbr[26] = 36
    fsevenbr[27] = 41
    fsevenbr[28] = 44
    fsevenbr[29] = 47
    fsevenbr[30] = 50
    fsevenbr[31] = 54
    fsevenbr[32] = 58
    fsevenbr[33] = 61
    fsevenbr[34] = 61
    fsevenbr[35] = 62
    fsevenbr[36] = 63
    fsevenbr[37] = 64
    fsevenbr[38] = 68
    fsevenbr[39] = 71
    fsevenbr[40] = 74
    fsevenbr[41] = 78
    fsevenbr[42] = 82
    fsevenbr[43] = 84
    fsevenbr[44] = 86
    fsevenbr[45] = 89
    fsevenbr[46] = 91
    fsevenbr[47] = 92
    fsevenbr[48] = 93
    fsevenbr[49] = 94
    fsevenbr[50] = 94
    fsevenbr[51] = 95
    fsevenbr[52] = 95
    fsevenbr[53] = 96
    fsevenbr[54] = 98
    fsevenbr[55] = 100
    fsevenbr[56] = 103
    fsevenbr[57] = 106
    fsevenbr[58] = 111
    fsevenbr[59] = 116
    fsevenbr[60] = 121
    return fsevenbr[fsevene]


def checkfeightabr(feightae):
    feightabr = [0] * 54
    feightabr[0] = 0
    feightabr[1] = 0
    feightabr[2] = 0
    feightabr[3] = 0
    feightabr[4] = 0
    feightabr[5] = 0
    feightabr[6] = 0
    feightabr[7] = 0
    feightabr[8] = 0
    feightabr[9] = 5
    feightabr[10] = 7
    feightabr[11] = 12
    feightabr[12] = 17
    feightabr[13] = 24
    feightabr[14] = 28
    feightabr[15] = 32
    feightabr[16] = 34
    feightabr[17] = 35
    feightabr[18] = 40
    feightabr[19] = 45
    feightabr[20] = 48
    feightabr[21] = 50
    feightabr[22] = 51
    feightabr[23] = 52
    feightabr[24] = 53
    feightabr[25] = 57
    feightabr[26] = 63
    feightabr[27] = 66
    feightabr[28] = 67
    feightabr[29] = 68
    feightabr[30] = 69
    feightabr[31] = 72
    feightabr[32] = 73
    feightabr[33] = 74
    feightabr[34] = 77
    feightabr[35] = 78
    feightabr[36] = 79
    feightabr[37] = 79
    feightabr[38] = 80
    feightabr[39] = 81
    feightabr[40] = 85
    feightabr[41] = 88
    feightabr[42] = 89
    feightabr[43] = 90
    feightabr[44] = 93
    feightabr[45] = 96
    feightabr[46] = 100
    feightabr[47] = 104
    feightabr[48] = 109
    feightabr[49] = 111
    feightabr[50] = 113
    feightabr[51] = 115
    feightabr[52] = 118
    feightabr[53] = 121
    return feightabr[feightae]


def checkfeightbbr(feightbe):
    feightbbr = [0] * 49
    feightbbr[0] = 0
    feightbbr[1] = 0
    feightbbr[2] = 0
    feightbbr[3] = 10
    feightbbr[4] = 15
    feightbbr[5] = 20
    feightbbr[6] = 25
    feightbbr[7] = 30
    feightbbr[8] = 34
    feightbbr[9] = 37
    feightbbr[10] = 40
    feightbbr[11] = 42
    feightbbr[12] = 45
    feightbbr[13] = 52
    feightbbr[14] = 58
    feightbbr[15] = 66
    feightbbr[16] = 67
    feightbbr[17] = 68
    feightbbr[18] = 69
    feightbbr[19] = 70
    feightbbr[20] = 71
    feightbbr[21] = 72
    feightbbr[22] = 74
    feightbbr[23] = 75
    feightbbr[24] = 75
    feightbbr[25] = 76
    feightbbr[26] = 76
    feightbbr[27] = 77
    feightbbr[28] = 78
    feightbbr[29] = 79
    feightbbr[30] = 80
    feightbbr[31] = 81
    feightbbr[32] = 83
    feightbbr[33] = 86
    feightbbr[34] = 87
    feightbbr[35] = 90
    feightbbr[36] = 92
    feightbbr[37] = 95
    feightbbr[38] = 99
    feightbbr[39] = 102
    feightbbr[40] = 104
    feightbbr[41] = 106
    feightbbr[42] = 106
    feightbbr[43] = 107
    feightbbr[44] = 108
    feightbbr[45] = 111
    feightbbr[46] = 116
    feightbbr[47] = 118
    feightbbr[48] = 121
    return feightbbr[feightbe]


def checkfsbr(fse):
    fsbr = [0] * 49
    fsbr[0] = 0
    fsbr[1] = 0
    fsbr[2] = 0
    fsbr[3] = 16
    fsbr[4] = 26
    fsbr[5] = 41
    fsbr[6] = 42
    fsbr[7] = 43
    fsbr[8] = 43
    fsbr[9] = 44
    fsbr[10] = 44
    fsbr[11] = 44
    fsbr[12] = 45
    fsbr[13] = 46
    fsbr[14] = 47
    fsbr[15] = 48
    fsbr[16] = 51
    fsbr[17] = 53
    fsbr[18] = 54
    fsbr[19] = 60
    fsbr[20] = 61
    fsbr[21] = 62
    fsbr[22] = 64
    fsbr[23] = 65
    fsbr[24] = 66
    fsbr[25] = 66
    fsbr[26] = 66
    fsbr[27] = 66
    fsbr[28] = 66
    fsbr[29] = 66
    fsbr[30] = 67
    fsbr[31] = 67
    fsbr[32] = 68
    fsbr[33] = 68
    fsbr[34] = 69
    fsbr[35] = 70
    fsbr[36] = 71
    fsbr[37] = 72
    fsbr[38] = 73
    fsbr[39] = 74
    fsbr[40] = 76
    fsbr[41] = 79
    fsbr[42] = 81
    fsbr[43] = 89
    fsbr[44] = 96
    fsbr[45] = 102
    fsbr[46] = 108
    fsbr[47] = 116
    fsbr[48] = 121
    return fsbr[fse]


def checkfcbr(fce):
    fcbr = [0] * 66
    fcbr[0] = 0
    fcbr[1] = 0
    fcbr[2] = 0
    fcbr[3] = 0
    fcbr[4] = 5
    fcbr[5] = 10
    fcbr[6] = 20
    fcbr[7] = 26
    fcbr[8] = 31
    fcbr[9] = 33
    fcbr[10] = 34
    fcbr[11] = 36
    fcbr[12] = 37
    fcbr[13] = 38
    fcbr[14] = 39
    fcbr[15] = 40
    fcbr[16] = 41
    fcbr[17] = 43
    fcbr[18] = 46
    fcbr[19] = 51
    fcbr[20] = 52
    fcbr[21] = 53
    fcbr[22] = 54
    fcbr[23] = 55
    fcbr[24] = 56
    fcbr[25] = 57
    fcbr[26] = 58
    fcbr[27] = 59
    fcbr[28] = 60
    fcbr[29] = 60
    fcbr[30] = 61
    fcbr[31] = 62
    fcbr[32] = 62
    fcbr[33] = 63
    fcbr[34] = 64
    fcbr[35] = 64
    fcbr[36] = 65
    fcbr[37] = 66
    fcbr[38] = 66
    fcbr[39] = 67
    fcbr[40] = 68
    fcbr[41] = 68
    fcbr[42] = 69
    fcbr[43] = 70
    fcbr[44] = 70
    fcbr[45] = 71
    fcbr[46] = 72
    fcbr[47] = 72
    fcbr[48] = 73
    fcbr[49] = 73
    fcbr[50] = 74
    fcbr[51] = 75
    fcbr[52] = 78
    fcbr[53] = 81
    fcbr[54] = 83
    fcbr[55] = 85
    fcbr[56] = 88
    fcbr[57] = 92
    fcbr[58] = 96
    fcbr[59] = 100
    fcbr[60] = 103
    fcbr[61] = 106
    fcbr[62] = 109
    fcbr[63] = 112
    fcbr[64] = 115
    fcbr[65] = 121
    return fcbr[fce]


def checkfpbr(fpe):
    fpbr = [0] * 60
    fpbr[0] = 7
    fpbr[1] = 7
    fpbr[2] = 7
    fpbr[3] = 12
    fpbr[4] = 17
    fpbr[5] = 22
    fpbr[6] = 27
    fpbr[7] = 32
    fpbr[8] = 37
    fpbr[9] = 40
    fpbr[10] = 42
    fpbr[11] = 43
    fpbr[12] = 45
    fpbr[13] = 47
    fpbr[14] = 49
    fpbr[15] = 52
    fpbr[16] = 53
    fpbr[17] = 57
    fpbr[18] = 62
    fpbr[19] = 67
    fpbr[20] = 67
    fpbr[21] = 67
    fpbr[22] = 67
    fpbr[23] = 67
    fpbr[24] = 67
    fpbr[25] = 67
    fpbr[26] = 67
    fpbr[27] = 67
    fpbr[28] = 67
    fpbr[29] = 67
    fpbr[30] = 67
    fpbr[31] = 67
    fpbr[32] = 67
    fpbr[33] = 67
    fpbr[34] = 67
    fpbr[35] = 67
    fpbr[36] = 67
    fpbr[37] = 67
    fpbr[38] = 69
    fpbr[39] = 71
    fpbr[40] = 73
    fpbr[41] = 75
    fpbr[42] = 77
    fpbr[43] = 80
    fpbr[44] = 82
    fpbr[45] = 84
    fpbr[46] = 86
    fpbr[47] = 88
    fpbr[48] = 90
    fpbr[49] = 92
    fpbr[50] = 96
    fpbr[51] = 100
    fpbr[52] = 104
    fpbr[53] = 107
    fpbr[54] = 109
    fpbr[55] = 111
    fpbr[56] = 114
    fpbr[57] = 117
    fpbr[58] = 119
    fpbr[59] = 121
    return fpbr[fpe]


def checkfabr(fae):
    fabr = [0] * 40
    fabr[0] = 0
    fabr[1] = 0
    fabr[2] = 0
    fabr[3] = 5
    fabr[4] = 10
    fabr[5] = 15
    fabr[6] = 20
    fabr[7] = 30
    fabr[8] = 32
    fabr[9] = 35
    fabr[10] = 37
    fabr[11] = 40
    fabr[12] = 42
    fabr[13] = 48
    fabr[14] = 52
    fabr[15] = 57
    fabr[16] = 60
    fabr[17] = 64
    fabr[18] = 68
    fabr[19] = 72
    fabr[20] = 75
    fabr[21] = 77
    fabr[22] = 80
    fabr[23] = 82
    fabr[24] = 85
    fabr[25] = 87
    fabr[26] = 88
    fabr[27] = 89
    fabr[28] = 91
    fabr[29] = 93
    fabr[30] = 95
    fabr[31] = 97
    fabr[32] = 99
    fabr[33] = 101
    fabr[34] = 103
    fabr[35] = 105
    fabr[36] = 107
    fabr[37] = 109
    fabr[38] = 112
    fabr[39] = 115
    return fabr[fae]


def checkfhbr(fhe):
    fhbr = [0] * 45
    fhbr[0] = 10
    fhbr[1] = 10
    fhbr[2] = 10
    fhbr[3] = 25
    fhbr[4] = 30
    fhbr[5] = 35
    fhbr[6] = 40
    fhbr[7] = 43
    fhbr[8] = 45
    fhbr[9] = 50
    fhbr[10] = 52
    fhbr[11] = 55
    fhbr[12] = 57
    fhbr[13] = 57
    fhbr[14] = 58
    fhbr[15] = 59
    fhbr[16] = 59
    fhbr[17] = 59
    fhbr[18] = 60
    fhbr[19] = 61
    fhbr[20] = 62
    fhbr[21] = 63
    fhbr[22] = 64
    fhbr[23] = 65
    fhbr[24] = 65
    fhbr[25] = 66
    fhbr[26] = 66
    fhbr[27] = 67
    fhbr[28] = 68
    fhbr[29] = 69
    fhbr[30] = 70
    fhbr[31] = 70
    fhbr[32] = 71
    fhbr[33] = 73
    fhbr[34] = 74
    fhbr[35] = 75
    fhbr[36] = 80
    fhbr[37] = 85
    fhbr[38] = 89
    fhbr[39] = 94
    fhbr[40] = 97
    fhbr[41] = 100
    fhbr[42] = 105
    fhbr[43] = 110
    fhbr[44] = 115
    return fhbr[fhe]


def checkfnbr(fne):
    fnbr = [0] * 46
    fnbr[0] = 0
    fnbr[1] = 0
    fnbr[2] = 0
    fnbr[3] = 0
    fnbr[4] = 5
    fnbr[5] = 7
    fnbr[6] = 9
    fnbr[7] = 12
    fnbr[8] = 15
    fnbr[9] = 18
    fnbr[10] = 25
    fnbr[11] = 30
    fnbr[12] = 35
    fnbr[13] = 37
    fnbr[14] = 40
    fnbr[15] = 42
    fnbr[16] = 45
    fnbr[17] = 47
    fnbr[18] = 50
    fnbr[19] = 52
    fnbr[20] = 55
    fnbr[21] = 57
    fnbr[22] = 60
    fnbr[23] = 60
    fnbr[24] = 60
    fnbr[25] = 60
    fnbr[26] = 60
    fnbr[27] = 60
    fnbr[28] = 60
    fnbr[29] = 61
    fnbr[30] = 62
    fnbr[31] = 64
    fnbr[32] = 65
    fnbr[33] = 67
    fnbr[34] = 68
    fnbr[35] = 70
    fnbr[36] = 73
    fnbr[37] = 74
    fnbr[38] = 76
    fnbr[39] = 79
    fnbr[40] = 81
    fnbr[41] = 84
    fnbr[42] = 90
    fnbr[43] = 97
    fnbr[44] = 110
    fnbr[45] = 115
    return fnbr[fne]


def checkfdbr(fde):
    fdbr = [0] * 58
    fdbr[0] = 0
    fdbr[1] = 0
    fdbr[2] = 0
    fdbr[3] = 0
    fdbr[4] = 0
    fdbr[5] = 0
    fdbr[6] = 0
    fdbr[7] = 0
    fdbr[8] = 0
    fdbr[9] = 5
    fdbr[10] = 10
    fdbr[11] = 15
    fdbr[12] = 19
    fdbr[13] = 22
    fdbr[14] = 25
    fdbr[15] = 27
    fdbr[16] = 29
    fdbr[17] = 31
    fdbr[18] = 33
    fdbr[19] = 35
    fdbr[20] = 37
    fdbr[21] = 39
    fdbr[22] = 41
    fdbr[23] = 44
    fdbr[24] = 46
    fdbr[25] = 53
    fdbr[26] = 58
    fdbr[27] = 61
    fdbr[28] = 65
    fdbr[29] = 70
    fdbr[30] = 74
    fdbr[31] = 76
    fdbr[32] = 77
    fdbr[33] = 79
    fdbr[34] = 82
    fdbr[35] = 86
    fdbr[36] = 88
    fdbr[37] = 89
    fdbr[38] = 90
    fdbr[39] = 91
    fdbr[40] = 91
    fdbr[41] = 91
    fdbr[42] = 91
    fdbr[43] = 92
    fdbr[44] = 92
    fdbr[45] = 92
    fdbr[46] = 93
    fdbr[47] = 93
    fdbr[48] = 93
    fdbr[49] = 94
    fdbr[50] = 95
    fdbr[51] = 96
    fdbr[52] = 97
    fdbr[53] = 98
    fdbr[54] = 100
    fdbr[55] = 105
    fdbr[56] = 110
    fdbr[57] = 115
    return fdbr[fde]


def checkfbbr(fbe):
    fbbr = [0] * 51
    fbbr[0] = 0
    fbbr[1] = 0
    fbbr[2] = 0
    fbbr[3] = 0
    fbbr[4] = 0
    fbbr[5] = 0
    fbbr[6] = 0
    fbbr[7] = 0
    fbbr[8] = 10
    fbbr[9] = 15
    fbbr[10] = 20
    fbbr[11] = 25
    fbbr[12] = 35
    fbbr[13] = 37
    fbbr[14] = 39
    fbbr[15] = 42
    fbbr[16] = 45
    fbbr[17] = 47
    fbbr[18] = 49
    fbbr[19] = 52
    fbbr[20] = 55
    fbbr[21] = 57
    fbbr[22] = 59
    fbbr[23] = 60
    fbbr[24] = 60
    fbbr[25] = 60
    fbbr[26] = 60
    fbbr[27] = 60
    fbbr[28] = 60
    fbbr[29] = 61
    fbbr[30] = 63
    fbbr[31] = 65
    fbbr[32] = 67
    fbbr[33] = 69
    fbbr[34] = 71
    fbbr[35] = 73
    fbbr[36] = 75
    fbbr[37] = 78
    fbbr[38] = 82
    fbbr[39] = 85
    fbbr[40] = 89
    fbbr[41] = 91
    fbbr[42] = 94
    fbbr[43] = 96
    fbbr[44] = 98
    fbbr[45] = 100
    fbbr[46] = 103
    fbbr[47] = 106
    fbbr[48] = 109
    fbbr[49] = 112
    fbbr[50] = 115
    return fbbr[fbe]


def checkftbr(fte):
    ftbr = [0] * 64
    ftbr[0] = 0
    ftbr[1] = 0
    ftbr[2] = 0
    ftbr[3] = 0
    ftbr[4] = 0
    ftbr[5] = 0
    ftbr[6] = 0
    ftbr[7] = 4
    ftbr[8] = 8
    ftbr[9] = 12
    ftbr[10] = 16
    ftbr[11] = 20
    ftbr[12] = 25
    ftbr[13] = 30
    ftbr[14] = 35
    ftbr[15] = 37
    ftbr[16] = 39
    ftbr[17] = 41
    ftbr[18] = 43
    ftbr[19] = 45
    ftbr[20] = 48
    ftbr[21] = 51
    ftbr[22] = 55
    ftbr[23] = 58
    ftbr[24] = 60
    ftbr[25] = 60
    ftbr[26] = 60
    ftbr[27] = 60
    ftbr[28] = 60
    ftbr[29] = 61
    ftbr[30] = 62
    ftbr[31] = 63
    ftbr[32] = 64
    ftbr[33] = 66
    ftbr[34] = 67
    ftbr[35] = 68
    ftbr[36] = 69
    ftbr[37] = 70
    ftbr[38] = 71
    ftbr[39] = 72
    ftbr[40] = 72
    ftbr[41] = 73
    ftbr[42] = 74
    ftbr[43] = 75
    ftbr[44] = 77
    ftbr[45] = 78
    ftbr[46] = 79
    ftbr[47] = 80
    ftbr[48] = 81
    ftbr[49] = 83
    ftbr[50] = 85
    ftbr[51] = 87
    ftbr[52] = 88
    ftbr[53] = 89
    ftbr[54] = 90
    ftbr[55] = 92
    ftbr[56] = 95
    ftbr[57] = 97
    ftbr[58] = 100
    ftbr[59] = 102
    ftbr[60] = 104
    ftbr[61] = 107
    ftbr[62] = 110
    ftbr[63] = 115
    return ftbr[fte]


def checkfssbr(fsse):
    fssbr = [0] * 48
    fssbr[0] = 0
    fssbr[1] = 0
    fssbr[2] = 0
    fssbr[3] = 35
    fssbr[4] = 38
    fssbr[5] = 40
    fssbr[6] = 42
    fssbr[7] = 45
    fssbr[8] = 47
    fssbr[9] = 55
    fssbr[10] = 60
    fssbr[11] = 60
    fssbr[12] = 60
    fssbr[13] = 60
    fssbr[14] = 60
    fssbr[15] = 60
    fssbr[16] = 60
    fssbr[17] = 60
    fssbr[18] = 60
    fssbr[19] = 60
    fssbr[20] = 60
    fssbr[21] = 62
    fssbr[22] = 62
    fssbr[23] = 64
    fssbr[24] = 65
    fssbr[25] = 67
    fssbr[26] = 69
    fssbr[27] = 70
    fssbr[28] = 72
    fssbr[29] = 73
    fssbr[30] = 75
    fssbr[31] = 80
    fssbr[32] = 81
    fssbr[33] = 83
    fssbr[34] = 85
    fssbr[35] = 87
    fssbr[36] = 89
    fssbr[37] = 90
    fssbr[38] = 95
    fssbr[39] = 97
    fssbr[40] = 98
    fssbr[41] = 99
    fssbr[42] = 100
    fssbr[43] = 102
    fssbr[44] = 104
    fssbr[45] = 105
    fssbr[46] = 110
    fssbr[47] = 115
    return fssbr[fsse]


def checkfccbr(fcce):
    fccbr = [0] * 49
    fccbr[0] = 0
    fccbr[1] = 0
    fccbr[2] = 0
    fccbr[3] = 10
    fccbr[4] = 25
    fccbr[5] = 35
    fccbr[6] = 45
    fccbr[7] = 47
    fccbr[8] = 50
    fccbr[9] = 52
    fccbr[10] = 53
    fccbr[11] = 54
    fccbr[12] = 55
    fccbr[13] = 56
    fccbr[14] = 57
    fccbr[15] = 58
    fccbr[16] = 59
    fccbr[17] = 60
    fccbr[18] = 60
    fccbr[19] = 60
    fccbr[20] = 60
    fccbr[21] = 60
    fccbr[22] = 60
    fccbr[23] = 60
    fccbr[24] = 60
    fccbr[25] = 60
    fccbr[26] = 61
    fccbr[27] = 61
    fccbr[28] = 62
    fccbr[29] = 64
    fccbr[30] = 66
    fccbr[31] = 67
    fccbr[32] = 69
    fccbr[33] = 71
    fccbr[34] = 72
    fccbr[35] = 73
    fccbr[36] = 76
    fccbr[37] = 77
    fccbr[38] = 78
    fccbr[39] = 79
    fccbr[40] = 80
    fccbr[41] = 81
    fccbr[42] = 82
    fccbr[43] = 83
    fccbr[44] = 88
    fccbr[45] = 95
    fccbr[46] = 100
    fccbr[47] = 110
    fccbr[48] = 115
    return fccbr[fcce]


def checkfppbr(fppe):
    fppbr = [0] * 37
    fppbr[0] = 0
    fppbr[1] = 0
    fppbr[2] = 0
    fppbr[3] = 15
    fppbr[4] = 35
    fppbr[5] = 37
    fppbr[6] = 40
    fppbr[7] = 45
    fppbr[8] = 55
    fppbr[9] = 60
    fppbr[10] = 60
    fppbr[11] = 60
    fppbr[12] = 60
    fppbr[13] = 60
    fppbr[14] = 60
    fppbr[15] = 60
    fppbr[16] = 61
    fppbr[17] = 62
    fppbr[18] = 64
    fppbr[19] = 65
    fppbr[20] = 67
    fppbr[21] = 70
    fppbr[22] = 71
    fppbr[23] = 73
    fppbr[24] = 74
    fppbr[25] = 76
    fppbr[26] = 82
    fppbr[27] = 86
    fppbr[28] = 87
    fppbr[29] = 88
    fppbr[30] = 91
    fppbr[31] = 94
    fppbr[32] = 97
    fppbr[33] = 100
    fppbr[34] = 105
    fppbr[35] = 110
    fppbr[36] = 115
    return fppbr[fppe]


def checkfybr(fye):
    fybr = [0] * 22
    fybr[0] = 0
    fybr[1] = 0
    fybr[2] = 0
    fybr[3] = 10
    fybr[4] = 20
    fybr[5] = 24
    fybr[6] = 28
    fybr[7] = 34
    fybr[8] = 35
    fybr[9] = 41
    fybr[10] = 45
    fybr[11] = 50
    fybr[12] = 57
    fybr[13] = 63
    fybr[14] = 67
    fybr[15] = 71
    fybr[16] = 75
    fybr[17] = 80
    fybr[18] = 85
    fybr[19] = 91
    fybr[20] = 95
    fybr[21] = 100
    return fybr[fye]


def checkfzbr(fze):
    fzbr = [0] * 36
    fzbr[0] = 0
    fzbr[1] = 15
    fzbr[2] = 25
    fzbr[3] = 34
    fzbr[4] = 35
    fzbr[5] = 37
    fzbr[6] = 40
    fzbr[7] = 43
    fzbr[8] = 45
    fzbr[9] = 46
    fzbr[10] = 48
    fzbr[11] = 49
    fzbr[12] = 51
    fzbr[13] = 52
    fzbr[14] = 54
    fzbr[15] = 55
    fzbr[16] = 57
    fzbr[17] = 59
    fzbr[18] = 61
    fzbr[19] = 63
    fzbr[20] = 65
    fzbr[21] = 67
    fzbr[22] = 69
    fzbr[23] = 71
    fzbr[24] = 73
    fzbr[25] = 75
    fzbr[26] = 78
    fzbr[27] = 82
    fzbr[28] = 85
    fzbr[29] = 87
    fzbr[30] = 88
    fzbr[31] = 90
    fzbr[32] = 92
    fzbr[33] = 94
    fzbr[34] = 97
    fzbr[35] = 100
    return fzbr[fze]


def male(w):
    rawbr = [0] * 25
    rawbr[1] = checkybr(w[1])
    rawbr[2] = checkzbr(w[2])
    rawbr[3] = checkonebr(w[3])
    rawbr[4] = checktwobr(w[4])
    rawbr[5] = checkthreebr(w[5])
    rawbr[6] = checkfourbr(w[6])
    rawbr[7] = checkfivebr(w[7])
    rawbr[8] = checksixabr(w[8])
    rawbr[9] = checksixbbr(w[9])
    rawbr[10] = checksevenbr(w[10])
    rawbr[11] = checkeightabr(w[11])
    rawbr[12] = checkeightbbr(w[12])
    rawbr[13] = checksbr(w[13])
    rawbr[14] = checkcbr(w[14])
    rawbr[15] = checkpbr(w[15])
    rawbr[16] = checkabr(w[16])
    rawbr[17] = checkhbr(w[17])
    rawbr[18] = checknbr(w[18])
    rawbr[19] = checkdbr(w[19])
    rawbr[20] = checkbbr(w[20])
    rawbr[21] = checktbr(w[21])
    rawbr[22] = checkssbr(w[22])
    rawbr[23] = checkccbr(w[23])
    rawbr[24] = checkppbr(w[24])
    return rawbr


def female(w):
    rawbr = [0] * 25
    rawbr[1] = checkfybr(w[1])
    rawbr[2] = checkfzbr(w[2])
    rawbr[3] = checkfonebr(w[3])
    rawbr[4] = checkftwobr(w[4])
    rawbr[5] = checkfthreebr(w[5])
    rawbr[6] = checkffourbr(w[6])
    rawbr[7] = checkffivebr(w[7])
    rawbr[8] = checkfsixabr(w[8])
    rawbr[9] = checkfsixbbr(w[9])
    rawbr[10] = checkfsevenbr(w[10])
    rawbr[11] = checkfeightabr(w[11])
    rawbr[12] = checkfeightbbr(w[12])
    rawbr[13] = checkfsbr(w[13])
    rawbr[14] = checkfcbr(w[14])
    rawbr[15] = checkfpbr(w[15])
    rawbr[16] = checkfabr(w[16])
    rawbr[17] = checkfhbr(w[17])
    rawbr[18] = checkfnbr(w[18])
    rawbr[19] = checkfdbr(w[19])
    rawbr[20] = checkfbbr(w[20])
    rawbr[21] = checkftbr(w[21])
    rawbr[22] = checkfssbr(w[22])
    rawbr[23] = checkfccbr(w[23])
    rawbr[24] = checkfppbr(w[24])
    return rawbr


def daadjust(rawbr, xcor):
    dcorrect = rawbr[19] + xcor
    acorrect = rawbr[16] + xcor
    if dcorrect >= 85:
        if acorrect < 85:
            return dcorrect - 85
        else:
            return acorrect + dcorrect - 170
    else:
        return 0


def ddadjust(rawbr):
    dd = (rawbr[1] - rawbr[2]) / 10
    if abs(dd - round(dd)) == .5:
        if dd == abs(dd):
            dd = dd + 0.1
        else:
            dd = dd - 0.1
    rdd = round(dd)
    if rdd > 10:
        rdd = 10
    if rdd < -10:
        rdd = -10
    return rdd


def dcadjust(fordc):
    g = 0
    gp = 0
    biggest = 0
    bigger = 0
    for j in range(3, 13):
        if biggest < fordc[j]:
            biggest = fordc[j]
            g = j
    for j in range(3, 13):
        if j == g:
            j = j + 1
        if (bigger < fordc[j]):
            bigger = fordc[j]
            gp = j
    return g, gp


def calculate_result(person, choices):
    w = [0] * 26
    r = [0] * 26

    v(person, choices, w, r)
    pp(person, choices, w, r)
    cc(person, choices, w, r)
    ss(person, choices, w, r)
    t(person, choices, w, r)
    b(person, choices, w, r)
    n(person, choices, w, r)
    d(person, choices, w, r)
    h(person, choices, w, r)
    a(person, choices, w, r)
    p(person, choices, w, r)
    c(person, choices, w, r)
    s(person, choices, w, r)
    eightb(person, choices, w, r)
    eighta(person, choices, w, r)
    seven(person, choices, w, r)
    sixb(person, choices, w, r)
    sixa(person, choices, w, r)
    five(person, choices, w, r)
    four(person, choices, w, r)
    three(person, choices, w, r)
    two(person, choices, w, r)
    one(person, choices, w, r)
    z(person, choices, w, r)
    y(person, choices, w, r)

    rawbr = [0] * 25
    if person.sex == 0:
        rawbr = male(w)
    else:
        rawbr = female(w)

    rawx = (w[6] + w[11]) * 1.5 + (w[3] + w[4] + w[5] + w[12]) * 1.6 + w[7] + w[8] + w[9] + w[10]
    rx = rawx - int(rawx)

    if (rx == 0.5):
        rawx = rawx + 0.1
    rrawx = round(rawx)

    xcor = 0
    hxcor = 0

    if rrawx in [
        145, 146, 147, 148, 149
    ]:
        xcor = 11
        hxcor = 5
    elif rrawx in [
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159
    ]:
        xcor = 10
        hxcor = 5
    elif rrawx in [
        160, 161, 162, 163, 164, 165, 166, 167, 168, 169
    ]:
        xcor = 9
        hxcor = 4
    elif rrawx in [
        170, 171, 172, 173, 174, 175, 176, 177, 178, 179
    ]:
        xcor = 8
        hxcor = 4
    elif rrawx in [
        180, 181, 182, 183, 184, 185, 186, 187, 188, 189
    ]:
        xcor = 7
        hxcor = 3
    elif rrawx in [
        190, 191, 192, 193, 194, 195, 196, 197, 198, 199
    ]:
        xcor = 6
        hxcor = 3
    elif rrawx in [
        200, 201, 202, 203, 204, 205, 206, 207, 208, 209
    ]:
        xcor = 5
        hxcor = 2
    elif rrawx in [
        210, 211, 212, 213, 214, 215, 216, 217, 218, 219
    ]:
        xcor = 4
        hxcor = 2
    elif rrawx in [
        220, 221, 222, 223, 224, 225, 226, 227, 228, 229
    ]:
        xcor = 3
        hxcor = 1
    elif rrawx in [
        230, 231, 232, 233, 234, 235, 236, 237, 238, 239
    ]:
        xcor = 2
        hxcor = 1
    elif rrawx in [
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249
    ]:
        xcor = 1
        hxcor = 0
    elif rrawx in [
        250, 251, 252, 253, 254, 255, 256, 257, 258, 259,
        260, 261, 262, 263, 264, 265, 266, 267, 268, 269,
        270, 271, 272, 273, 274, 275, 276, 277, 278, 279,
        280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
        290, 291, 292, 293, 294, 295, 296, 297, 298, 299,
        300, 301, 302, 303, 304, 305, 306, 307, 308, 309,
        310, 311, 312, 313, 314, 315, 316, 317, 318, 319,
        320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
        330, 331, 332, 333, 334, 335, 336, 337, 338, 339,
        340, 341, 342, 343, 344, 345, 346, 347, 348, 349,
        350, 351, 352, 353, 354, 355, 356, 357, 358, 359,
        360, 361, 362, 363, 364, 365, 366, 367, 368, 369,
        370, 371, 372, 373, 374, 375, 376, 377, 378, 379,
        380, 381, 382, 383, 384, 385, 386, 387, 388, 389,
        390, 391, 392, 393, 394, 395, 396, 397, 398, 399,
        400
    ]:
        xcor = 0
        hxcor = 0
    elif rrawx in [
        401, 402, 403, 404, 405, 406, 407, 408, 409, 410,
        411, 412, 413, 414, 415, 416
    ]:
        xcor = -1
        hxcor = 0
    elif rrawx in [
        417, 418, 419, 420, 421, 422, 423, 424, 425, 426,
        427, 428, 429, 430, 431, 432
    ]:
        xcor = -2
        hxcor = -1
    elif rrawx in [
        433, 434, 435, 436, 437, 438, 439, 440, 441, 442,
        443, 444, 445, 446, 447, 448
    ]:
        xcor = -3
        hxcor = -1
    elif rrawx in [
        449, 450, 451, 452, 453, 454, 455, 456, 457, 458,
        459, 460, 461, 462, 463, 464
    ]:
        xcor = -4
        hxcor = -2
    elif rrawx in [
        465, 466, 467, 468, 469, 470, 471, 472, 473, 474,
        475, 476, 477, 478, 479, 480
    ]:
        xcor = -5
        hxcor = -2
    elif rrawx in [
        481, 482, 483, 484, 485, 486, 487, 488, 489, 490,
        491, 492, 493, 494, 495, 496
    ]:
        xcor = -6
        hxcor = -3
    elif rrawx in [
        497, 498, 499, 500, 501, 502, 503, 504, 505, 506,
        507, 508, 509, 510, 511, 512
    ]:
        xcor = -7
        hxcor = -3
    elif rrawx in [
        513, 514, 515, 516, 517, 518, 519, 520, 521, 522,
        523, 524, 525, 526, 527, 528
    ]:
        xcor = -8
        hxcor = -4
    elif rrawx in [
        529, 530, 531, 532, 533, 534, 535, 536, 537, 538,
        539, 540, 541, 542, 543, 544
    ]:
        xcor = -9
        hxcor = -4
    elif rrawx in [
        545, 546, 547, 548, 549, 550, 551, 552, 553, 554,
        555, 556, 557, 558, 559, 560
    ]:
        xcor = -10
        hxcor = -5
    elif rrawx in [
        561, 562, 563, 564, 565, 566, 567, 568, 569, 570,
        571, 572, 573, 574, 575, 576
    ]:
        xcor = -11
        hxcor = -5
    elif rrawx in [
        577, 578, 579, 580, 581, 582, 583, 584, 585, 586,
        587, 588, 589, 590
    ]:
        xcor = -12
        hxcor = -6
    else:
        return {}

    if rrawx < 180:
        xscore = 0
    if rrawx > 180 and rrawx < 195:
        xscore = 5
    if rrawx > 194 and rrawx < 207:
        xscore = 10
    if rrawx > 206 and rrawx < 220:
        xscore = 15
    if rrawx > 219 and rrawx < 232:
        xscore = 20
    if rrawx > 231 and rrawx < 245:
        xscore = 25
    if rrawx > 244 and rrawx < 257:
        xscore = 30
    if rrawx > 256 and rrawx < 270:
        if person.sex == 0:
            xscore = 35
        else:
            xscore = 34

    if rrawx > 269 and rrawx < 282:
        xscore = 40
    if rrawx > 281 and rrawx < 295:
        xscore = 45
    if rrawx > 294 and rrawx < 307:
        xscore = 50
    if rrawx > 306 and rrawx < 320:
        if person.sex == 0:
            xscore = 55
        else:
            xscore = 54

    if rrawx > 319 and rrawx < 345:
        if person.sex == 0:
            xscore = 60
        else:
            xscore = 55

    if rrawx > 344 and rrawx < 357:
        if person.sex == 0:
            xscore = 63
        else:
            xscore = 56

    if rrawx > 356 and rrawx < 370:
        if person.sex == 0:
            xscore = 66
        else:
            xscore = 58

    if rrawx > 369 and rrawx < 382:
        if person.sex == 0:
            xscore = 69
        else:
            xscore = 60

    if rrawx > 381 and rrawx < 395:
        if person.sex == 0:
            xscore = 72
        else:
            xscore = 63

    if rrawx > 394 and rrawx < 420:
        if person.sex == 0:
            xscore = 74
        else:
            xscore = 65

    if rrawx > 419 and rrawx < 432:
        if person.sex == 0:
            xscore = 77
        else:
            xscore = 67

    if rrawx > 431 and rrawx < 445:
        if person.sex == 0:
            xscore = 79
        else:
            xscore = 70

    if rrawx > 444 and rrawx < 457:
        if person.sex == 0:
            xscore = 81
        else:
            xscore = 72

    if rrawx > 456 and rrawx < 470:
        if person.sex == 0:
            xscore = 83
        else:
            xscore = 75

    if rrawx > 469 and rrawx < 483:
        if person.sex == 0:
            xscore = 85
        else:
            xscore = 79

    if rrawx > 482 and rrawx < 495:
        if person.sex == 0:
            xscore = 87
        else:
            xscore = 84

    if rrawx > 494 and rrawx < 508:
        xscore = 89
    if rrawx > 507 and rrawx < 520:
        xscore = 91
    if rrawx > 519 and rrawx < 533:
        xscore = 93
    if rrawx > 532 and rrawx < 545:
        xscore = 95
    if rrawx > 544 and rrawx < 558:
        xscore = 97
    if rrawx > 557:
        xscore = 100

    dacontain = daadjust(rawbr, xcor)
    ddcontain = ddadjust(rawbr)

    inpadjust = person.duration_of_hospitalization + 1

    afterinp = [0] * 26
    afterall = [0] * 26

    if inpadjust in [1, 4]:
        da = int(0.25 * dacontain)
        if da > 15:
            da = 15
        dac = int(0.5 * dacontain)
        if dac > 10:
            dac = 10
    elif inpadjust == 2:
        da = dacontain
        if da > 25:
            da = 25
        dac = dacontain
        if dac > 20:
            dac = 20
        afterinp[22] = afterinp[22] + 8
        afterinp[23] = afterinp[23] + 10
        afterinp[24] = afterinp[24] + 4
    elif inpadjust == 3:
        da = int(0.5 * dacontain)
        if da > 15:
            da = 15
        dac = int(0.75 * dacontain)
        if dac > 15:
            dac = 15
        afterinp[22] = afterinp[22] + 5
        afterinp[23] = afterinp[23] + 7
        afterinp[24] = afterinp[24] + 2
    elif inpadjust == 5:
        da = int(0.5 * dacontain)
        if da > 15:
            da = 15
        dac = int(0.75 * dacontain)
        if dac > 15:
            dac = 15

    gg = [0] * 25
    gg[1] = "Y"
    gg[2] = "Z"
    gg[3] = "1"
    gg[4] = "2"
    gg[5] = "3"
    gg[6] = "4"
    gg[7] = "5"
    gg[8] = "6A"
    gg[9] = "6B"
    gg[10] = "7"
    gg[11] = "8A"
    gg[12] = "8B"
    gg[13] = "S"
    gg[14] = "C"
    gg[15] = "P"
    gg[16] = "A"
    gg[17] = "H"
    gg[18] = "N"
    gg[19] = "D"
    gg[20] = "B"
    gg[21] = "T"
    gg[22] = "SS"
    gg[23] = "CC"
    gg[24] = "PP"

    dabr = [0] * 26
    aftercor = [0] * 26
    afterhcor = [0] * 26
    afterddcor = [0] * 26
    afterdccor = [0] * 26

    for i in range(1, 25):
        if i == 1 or i == 2 or i == 13 or i == 14 or i == 15 or i == 22 or i == 23 or i == 24:
            aftercor[i] = ""
        else:
            aftercor[i] = rawbr[i] + xcor

        if i == 13 or i == 14 or i == 15 or i == 22 or i == 23 or i == 24:
            afterhcor[i] = rawbr[i] + hxcor
        else:
            afterhcor[i] = ""

        if i == 4 or i == 12:
            dabr[i] = aftercor[i] - da
        elif i == 14:
            dabr[i] = afterhcor[i] - dac
        else:
            dabr[i] = ""

        if i == 13:
            afterddcor[i] = afterhcor[i] + ddcontain
        elif i == 14:
            afterddcor[i] = dabr[i] + ddcontain
        elif i == 16 or i == 17 or i == 19:
            afterddcor[i] = aftercor[i] + ddcontain
        else:
            afterddcor[i] = ""

        fordc = [0] * 26
        if i == 4 or i == 12:
            fordc[i] = dabr[i]
        else:
            fordc[i] = aftercor[i]

        g = 0
        gp = 0
        if i == 13:
            g, gp = dcadjust(fordc)

        afterdccor[i] = ""
        if i > 12:
            if i in [13, 14, 16, 17, 19]:
                afterdccor[i] = afterddcor[i]
            elif i == 15:
                afterdccor[i] = afterhcor[i]
            else:
                afterdccor[i] = ""
            if g == 6 or g == 7 or g == 10 or gp == 10:
                if i in [13, 14]:
                    afterdccor[i] = afterdccor[i] + 4
                elif i == 15:
                    afterdccor[i] = afterdccor[i] + 2
                elif i in [16, 19]:
                    afterdccor[i] = afterdccor[i] + 15
                elif i == 17:
                    afterdccor[i] = afterdccor[i] + 13
            if g == 12 or g == 4 or gp == 4:
                if i == 13:
                    afterdccor[i] = afterdccor[i] - 2
                elif i in [14, 15]:
                    afterdccor[i] = afterdccor[i] - 6
                elif i == 16:
                    afterdccor[i] = afterdccor[i] - 7
                elif i in [17, 19]:
                    afterdccor[i] = afterdccor[i] - 5

        if i == 22 or i == 23 or i == 24:
            afterinp[i] = afterhcor[i] + afterinp[i]
        else:
            afterinp[i] = ""

        if i in [1, 2]:
            afterall[i] = rawbr[i]
        elif i in [3, 5, 6, 7, 8, 9, 10, 11, 18, 20, 21]:
            afterall[i] = aftercor[i]
        elif i in [4, 12]:
            afterall[i] = dabr[i]
        elif i in [13, 14, 15, 16, 17, 19]:
            afterall[i] = afterdccor[i]
        elif i in [22, 23, 24]:
            afterall[i] = afterinp[i]

    supplements = [
        [0],
        [0],
        [0],
        [13],
        [0],
        [0],
        [7],
        [6],
        [14],
        [0],
        [16],
        [0],
        [0],
        [3],
        [8, 18],
        [0],
        [10],
        [0],
        [14],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]

    states = [0]
    for i in range(1, 25):
        state = 0 if afterall[i] < 80 else 1 if afterall[i] < 90 else 2
        for supplement in supplements[i]:
            if state == 1 and afterall[supplement] > 80:
                state = 2
        states.append(state)

    return {
        'items': [{
            'name': r[i],
            'gg': gg[i],
            'r': r[i],
            'w': w[i],
            'rawbr': rawbr[i],
            'aftercor': aftercor[i],
            'afterhcor': afterhcor[i],
            'dabr': dabr[i],
            'afterddcor': afterddcor[i],
            'afterdccor': afterdccor[i],
            'afterinp': afterinp[i],
            'final_br': afterall[i],
            'state': states[i]
        } for i in range(1, 25)]
    }
