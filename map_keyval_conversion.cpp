#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

void strsplit(const string &line, string &key, std::set<string> &values, char c)
{
    size_t pos = line.find(c);
    size_t initialPos = 0;
    values.clear();
    int first_flag = 1;
    while (pos != std::string::npos) {
        if (first_flag == 1) {
            key = line.substr(initialPos, pos - initialPos);
            first_flag = 0;
        } else {
            string v = line.substr(initialPos, pos - initialPos);
            if (v[v.length()-1] == ',') v = v.substr(0, v.length()-1);
            values.insert(v);
        }
        initialPos = pos + 1;
        pos = line.find(c, initialPos);
    }
    values.insert(line.substr(initialPos, std::min(pos, line.size()) - initialPos + 1));
}

int main() {
    int n;
    string line, key;
    getline(std::cin, line);
    n = stoi(line);
    map<string, set<string>> el_dict, le_dict;
    for (int i = 0; i < n; ++i) {
        set<string> values;
        getline(std::cin, line);
        // cout << line << endl;
        strsplit(line, key, values, ' ');
        for (auto &s : values) {
            if (s == "-") values.erase(s);
        }
        el_dict.insert(make_pair(key, values));
    }
    for (auto &q: el_dict) {
        key = q.first;
        set<string> &values = q.second;
        for(auto &z: values) {
            auto p = le_dict.find(z);
            if (p != le_dict.end()) {
                (*p).second.insert(key);
            } else {
                set<string> le_values;
                le_values.insert(key);
                le_dict.insert(make_pair(z, le_values));
            }
        }
    }
    cout << le_dict.size() << endl;
    for (auto &q: le_dict) {
        cout << q.first << " - ";
        line = "";
        for(auto &z: q.second) line += (z + ", ");
        line = line.substr(0, line.length()-2);
        cout << line << endl;
    }
    return 0;
}
