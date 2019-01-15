#include <algorithm>
#include <iterator>

//пример вызова
std::set_difference(A.begin(), A.end(), B.begin(), B.end(), std::back_inserter(result));
//std::set_intersection
//std::set_union
//std::set_symmetric_difference -- элементы только в A или в B, но не в их пересечении
//std::merge
//std::inplace_merge -- меняет одно из множеств, мержит прямо в него

//проверка на вхождение одного множества в другое
bool AincludesB = std::includes(A.begin(), A.end(), B.begin(), B.end());
