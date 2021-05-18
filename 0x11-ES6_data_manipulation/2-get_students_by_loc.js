export default function getStudentsByLocation(array, city) {
  return array.filter((items) => items.location === city);
}
