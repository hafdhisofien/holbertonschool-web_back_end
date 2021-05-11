import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photo;
  let user;

  try {
    photo = await uploadPhoto();
    user = await createUser();
    return {
      photo,
      user,
    };
  } catch (e) {
    return {
      photo: null,
      user: null,
    };
  }
}
