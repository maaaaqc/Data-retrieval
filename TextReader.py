import collections
import re
from pathlib import Path


def extract_info(folder):
    DICTIONARY = collections.OrderedDict()
    onlyfiles = list(folder.glob('*.txt'))
    for file in onlyfiles:
        if not file.stem == "profile" \
            and not file.stem == "nlpsinfo" \
            and not "ccss" in file.stem:
            strings = []
            f = open(file, "r")
            content = f.readlines()
            for line in content:
                strings.append(line.strip().split(" ")[1].strip())
            strings.sort()
            DICTIONARY[file.stem] = strings
        elif file.stem == "nlpsinfo":
            strings = []
            results = []
            f = open(file, "r")
            content = f.read().split(";")
            strings.append([content[0].strip(), content[1].strip()])
            spec = content[2]
            pattern = re.compile('".+",".+"')
            results.extend(re.findall(pattern, spec))
            results.sort()
            for i in results:
                info = i.strip().replace('"','').replace('Version: ', '').split(",")
                strings.append(info)
            DICTIONARY[file.stem] = strings
        elif file.stem == "profile":
            strings = []
            results = []
            with open(file, "r") as f:
                content = " ".join(" ".join(f.read().strip().splitlines()).split())
                content = content.replace('" "', '";"')
                lines = content.split(";")
                pattern = re.compile('".+",".+",".+"')
                for line in lines:
                    match = re.match(pattern, line)
                    if match:
                        results.append(match.group(0))
                results[1:] = sorted(results[1:])
                for i in results:
                    info = i.strip().replace('"','').split(",")
                    if len(info) >= 4:
                        for index in range(3,len(info)):
                            info[2] = " ".join((info[2] + ", " + info[index]).strip().split())
                        del info[3:len(info)]
                    strings.append(info)
                DICTIONARY[file.stem] = strings
        elif "ccss" in file.stem:
            strings = []
            with open(file, "r") as f:
                content = f.readlines()
                content.sort()
                for string in content:
                    if not string.strip() == "":
                        if re.match('^".*"$', string.strip()):
                            info = string.strip().replace('"','').split(",")
                            strings.append(info)
                DICTIONARY[file.stem] = strings
    return DICTIONARY