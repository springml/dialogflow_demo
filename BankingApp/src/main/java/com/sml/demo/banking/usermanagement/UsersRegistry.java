package com.sml.demo.banking.usermanagement;

import java.util.HashMap;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class UsersRegistry {
    private static HashMap<String,User> users = new HashMap<>();
    public static void addUser(User user){
        users.put(user.getUserId(),user);
    }

    public static User getUser(String userId){
        return users.get(userId);
    }

    public static void removeUser(String userId){
        users.remove(userId);
    }
    public void clearRegistry(){
        users.clear();
    }
}
