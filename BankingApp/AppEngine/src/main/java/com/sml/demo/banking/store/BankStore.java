package com.sml.demo.banking.store;


import com.google.cloud.datastore.*;



import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.GeneralSecurityException;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

/**
 * Created by kaarthikraaj on 24/10/17.
 */
public class BankStore {


    private static BankStore dataStoreManager;
    //Only datastore instance that AdcountManager access.
    private static final Datastore datastore;
    private Logger logger =
            Logger.getLogger(BankStore.class.getName());
    //Entity's kind
    private final String kind = "BankAccounts";

    static {
        datastore = DatastoreOptions.getDefaultInstance().getService();
    }

    /*
    Singleton instance returned
     */
    public static synchronized BankStore getInstance() {

        if (dataStoreManager == null) {
            dataStoreManager = new BankStore();
        }
        return dataStoreManager;
    }



    /*
    Gets the current day's display count for the advertisement requested
    @param adId The advertisement identifier for which the display count
                is requested for the current day which has the properties
    @param Th display count for the current day for the given adId
    This method is called during threshold limit check step
     */
    public String getProperty(String entityName,String propertyName) {
        String value="";
        Key entityKey = this.getEntityKey(entityName);
        Entity userBankRecord = datastore.get(entityKey);
        if(userBankRecord!=null) {
            try {
                if(propertyName.equalsIgnoreCase("MobileNumber"))
                    value = userBankRecord.getString(propertyName);
                else
                    if(propertyName.equalsIgnoreCase("AccountBalance"))
                        value +=(userBankRecord.getLong(propertyName));

            } catch (DatastoreException dataStoreException) {
                logger.warning("Exception while getting property value for the given entity" + dataStoreException.getMessage());
            }
        }
        else{
            logger.warning("No record found");
        }
        return value;
    }

    private Key getEntityKey(String entityName) {
        Key entityKey;
        entityKey = datastore.newKeyFactory().setKind(kind).newKey(Long.parseLong(entityName));
        return entityKey;
    }

        public static void main(String[] args)  {
           BankStore bankStore =  BankStore.getInstance();
           System.out.println(bankStore.getProperty("kaarthikraaj","MobileNumber"));
            System.out.println(bankStore.getProperty("kaarthikraaj","AccountBalance"));

        }


}
