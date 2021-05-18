export default function getListStudentIds(array) {
  return array.reduce((accumulator, items) => accumulator + items.id, 0);
}
