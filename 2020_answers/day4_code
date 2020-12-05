def valid_passports(input_file):
    valid_passport_num = 0
    passport_file = open(input_file, "r")
    # Lines = passport_file.readlines()
    passport_array = passport_file.read().split("\n\n")


    print(passport_array)


    iyr = None
    byr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None

    for j in passport_array:
        byr = j.find("byr:")
        iyr = j.find("iyr:")
        eyr = j.find("eyr:")
        hgt = j.find("hgt:")
        hcl = j.find("hcl:")
        ecl = j.find("ecl:")
        pid = j.find("pid:")

        #print(byr, iyr, eyr, hgt, hcl, ecl, pid)
        if (byr >= 0) and (iyr >= 0) and (eyr >= 0) and (hgt >= 0) and (hcl >= 0) and (ecl >= 0) and (pid >= 0):
            curr_passport = j.split()
            current_dict = {}

            for k in curr_passport:
                current_dict[k.split(":")[0]] = k.split(":")[1]

            byr_valid = False
            if 1920 <= int(current_dict["byr"]) <= 2002:
                byr_valid = True
            iyr_valid = False
            if 2010 <= int(current_dict["iyr"]) <= 2020:
                iyr_valid = True
            eyr_valid = False
            if 2020 <= int(current_dict["eyr"]) <= 2030:
                eyr_valid = True
            hgt_valid = False
            if current_dict["hgt"].endswith("cm"):
                curr_num = current_dict["hgt"].replace("cm", "")
                if 150 <= int(curr_num) <= 193:
                    hgt_valid = True
            elif current_dict["hgt"].endswith("in"):
                curr_num = current_dict["hgt"].replace("in", "")
                if 59 <= int(curr_num) <= 76:
                    hgt_valid = True
                
            hcl_valid = False
            if current_dict["hcl"][0] == "#":
                hcl_valid = True
                for i in current_dict["hcl"][1:]:
                    if i not in "0123456789abcdef":
                        hcl_valid = False
            ecl_valid = False
            if current_dict["ecl"] == "amb" or current_dict["ecl"] == "blu" or current_dict["ecl"] == "brn" or current_dict["ecl"] == "gry" or current_dict["ecl"] == "grn" or current_dict["ecl"] == "hzl" or current_dict["ecl"] == "oth":
                ecl_valid = True
            pid_valid = False
            if len(current_dict["pid"]) == 9:
                pid_valid = True
                for j in current_dict["pid"]:
                    if j not in "0123456789":
                        pid_valid = False
            
            if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
                valid_passport_num += 1
    return valid_passport_num

print(valid_passports("day4_input.txt"))
